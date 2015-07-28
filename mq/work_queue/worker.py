import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare('task_queue', durable=True)


# with no ack
def callback_no_ack(ch, method, properties, body):
    print "[x] Received %r" % (body, )
    time.sleep(body.count('.'))
    print "[x] Done"


def callback(ch, method, properties, body):
    print "[x] Received %r" % (body, )
    time.sleep(body.count('.'))
    print "[x] Done"
    ch.basic_ack(delivery_tag=method.delivery_tag)


# channel.basic_consume(callback, queue='hello', no_ack=True)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='task_queue')
channel.start_consuming()