import socket as s
import threading

# Crea un socket client UDP
udp_client_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)

# Definisce l'indirizzo del server e la porta
server_address = ("192.168.1.21", 6980)

# Definisce la dimensione del buffer per la ricezione dei dati
BUFFER_SIZE = 4092

# Invia un messaggio iniziale per connettersi al server
udp_client_socket.sendto(b'Ciao server!', server_address)

# Thread per ricevere messaggi
def ricevi_messaggi():
    while True:
        try:
            data, address = udp_client_socket.recvfrom(BUFFER_SIZE)
            print(f"Messaggio ricevuto dal server: {data.decode()} da {address}")
        except Exception as e:
            print(f"Errore durante la ricezione: {e}")
            break

# Thread per inviare messaggi
def invia_messaggi():
    while True:
        try:
            message = input("Client: ")
            udp_client_socket.sendto(message.encode(), server_address)
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
udp_client_socket.close()
