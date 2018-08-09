import socket
HOST = 'localhost'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp recebe uma instancia da API socket
dest = (HOST, PORT) #destino da mensagem
tcp.connect(dest) #conecta com o tcp recebendo o destino como parametro
print 'Para sair use CTRL+X\n'
msg = raw_input() #lê do teclado
while msg <> '\x18': #enquanto for diferente de ctrl+x
    tcp.send (msg) #envia a mensagem
    msg = raw_input() #lê do teclado
tcp.close() #fecha o tcp