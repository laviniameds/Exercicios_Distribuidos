#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) #cria a conexao
channel = connection.channel()#abre o canal

channel.queue_declare(queue='eae')#declara o nome da queue

channel.basic_publish(exchange='',
                      routing_key='eae',
                      body='EAEEEE') #publicar no canal usando a chave e a mensagem

print(" [x] Enviou 'EAE MEN KK'")
connection.close()