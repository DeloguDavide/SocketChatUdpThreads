import socket

# Definisco l'indirizzo IP e la porta del server
server_address = ("192.168.65.19", 6980)  # 2 dati in una tupla, ip e porta

# Definisco la dimensione del buffer per la ricezione dei dati
BUFFER_SIZE = 4092  # quando ricevo dei dati, dichiaro quanti byte usare, se mando qualcosa di più grande avvengono troncamenti

# Creo una nuova socket UDP
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# AF_INET indica che la socket deve utilizzare il protocollo IPv4
# SOCK_DGRAM indica che la socket deve utilizzare il protocollo UDP

# Associa la socket all'indirizzo IP e alla porta del server
udp_server_socket.bind(server_address)
# La socket è ora in ascolto sull'indirizzo IP e la porta specificati

# Metto la socket in ascolto e attendo la ricezione di dati
data, client_address = udp_server_socket.recvfrom(BUFFER_SIZE)
# recvfrom() riceve i dati e restituisce due valori: data (i dati ricevuti) e address (l'indirizzo IP e la porta del client che ha inviato i dati)

# Stampo un messaggio che indica che i dati sono stati ricevuti
print(f"Messaggio ricevuto: {data.decode()} da {client_address}")
# decode() converte i dati ricevuti (che sono in formato binario) in una stringa di testo leggibile

#Invio messaggio al client
udp_server_socket.sendto("Benvenuto nel server!".encode("utf-8"), client_address)

#Chiudo
udp_server_socket.close()


