import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))

channel = connection.channel()
channel.exchange_declare(exchange='agent', type='direct')
channel.queue_declare(queue='cc')
channel.queue_bind(exchange='agent', queue='cc', routing_key='cc')


def on_request(ch, method, props, body):

    response = '{"abc":"def"}'
    print body
    header = {'status': 'successful'}
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=
                                                     props.correlation_id, headers=header),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='cc')

print " [x] Awaiting RPC requests"
channel.start_consuming()