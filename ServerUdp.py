import socket
import threading

# Definisco l'indirizzo IP e la porta del server
server_address = ("192.168.1.21", 6980)

# Definisco la dimensione del buffer per la ricezione dei dati
BUFFER_SIZE = 4092

# Creo una nuova socket UDP
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Associa la socket all'indirizzo IP e alla porta del server
udp_server_socket.bind(server_address)

# Variabile per gestire l'indirizzo del client
client_address = None

# Thread per ricevere messaggi dai client
def ricevi_messaggi():
    global client_address
    while True:
        try:
            data, address = udp_server_socket.recvfrom(BUFFER_SIZE)
            print(f"Messaggio ricevuto dal client: {data.decode()} da {address}")
            client_address = address
            
        except Exception as e:
            print(f"Errore durante la ricezione: {e}")
            break

# Thread per inviare messaggi al client
def invia_messaggi():
    global client_address
    while True:
        if client_address:  # Verifica se c'è un client connesso
            try:
                message = input("Server: ")
                udp_server_socket.sendto(message.encode(), client_address)
            except Exception as e:
                print(f"Errore durante l'invio: {e}")
                break

# Crea i thread
ricevi_thread = threading.Thread(target=ricevi_messaggi)
invia_thread = threading.Thread(target=invia_messaggi)

# Avvia i thread
ricevi_thread.start()
invia_thread.start()

# Unisci i thread per mantenerli attivi fino alla fine
ricevi_thread.join()
invia_thread.join()

# Chiudi la socket alla fine
udp_server_socket.close()
