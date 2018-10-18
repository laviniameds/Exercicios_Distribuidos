#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) #cria a conexao
channel = connection.channel() #se conecta ao canal

channel.queue_declare(queue='eae') #declara uma queue

def callback(ch, method, properties, body):
    print(" [x] Recebido %r" % body) #define um metodo de callback que vai receber a mensagem

channel.basic_consume(callback,
                      queue='eae',
                      no_ack=True) #chama o metodo passando a queue

print(' [*] Esperando mensagens. Para sair aperte CTRL+C')
channel.start_consuming() #começa a consumir o canal