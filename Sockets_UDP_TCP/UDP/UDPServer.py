import socket
HOST = 'localhost'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #datagram
orig = (HOST, PORT)
udp.bind(orig)
while True:
    msg, cliente = udp.recvfrom(1024)
    print cliente, msg
udp.close()