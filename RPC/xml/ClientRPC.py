import xmlrpc.client #importa a biblioteca RPC xml do lado cliente

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy: #define um proxy
    print("3 é par: %s" % str(proxy.is_even(3))) #chama a função que está definida no servidor passando o parametro
    print("100 é par: %s" % str(proxy.is_even(100)))