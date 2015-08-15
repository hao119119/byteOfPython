import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost', credentials=pika.credentials.PlainCredentials('guest', 'guest')))
channel = connection.channel()

channel.exchange_declare(exchange='ceilometer',
                         type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = ['heart_beating', 'metering']

for binding_key in binding_keys:
    channel.queue_bind(exchange='ceilometer',
                       queue=queue_name,
                       routing_key=binding_key)


def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()