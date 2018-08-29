import socket
HOST = 'localhost'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp recebe uma instancia da API socket
orig = (HOST, PORT) #origem da mensagem
tcp.bind(orig) #"ativa" as informações do socket
tcp.listen(1) #coloca o socket em modo passivo, esperando uma requisição
while True:
    con, cliente = tcp.accept() #aceita a requisição do cliente
    print 'Concetado por', cliente
    while True:
        msg = con.recv(1024) #recebe a mensagem
        if not msg: break
        print cliente, msg
    print 'Finalizando conexao do cliente', cliente
    con.close()