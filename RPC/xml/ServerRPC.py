from xmlrpc.server import SimpleXMLRPCServer #importa a biblioteca de RPC com XML do lado servidor

def is_even(n):
    print("Requisição recebida com o seguinte argumento: " + str(n))
    return n % 2 == 0

server = SimpleXMLRPCServer(("localhost", 8000)) #define a porta do servidor
print("Escutando na porta 8000...")
server.register_function(is_even, "is_even") #recebe a funcao is_even com parametros
server.serve_forever() #define que o servidor vai receber requisições enquato não houver uma exceção (shutdown)

print(server.xml)