import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='10.68.28.123', credentials=pika.credentials.PlainCredentials('openstack', '123456a?')))
channel = connection.channel()

channel.exchange_declare(exchange='cloud-agent', type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='cloud-agent', queue=queue_name, routing_key='agent')

print '[*] Waiting for logs, To exit press CTRL+C'


def callback(ch, method, properties, body):
    print "[x] %r:%r" % (method.routing_key, body)


channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()
