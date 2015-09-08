import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost', credentials=pika.credentials.PlainCredentials('guest', 'guest')))

channel = connection.channel()
channel.exchange_declare(exchange='agent', type='direct')

# message = {'context': {'a': 'a'},
#            "header": {
#                "version": "1.0",
#                "content_encoding": "UTF-8",
#                "type": "SERVICE",
#                "content_type": "application/json",
#                "isSuccessful": True,
#                "exchange": 'cloud-agent',
#                "routingKey": 'agent'
#            },
#            'commands': ['mkdir -p /home/cc/test', 'cd /home/cc/test', 'mkdir 123456']
#            }

message = {
"context": {
"clusterId": "cluster-id-1",
"componentId": "entity-id-1",
"serverId": "6815a0135a914e3187d2e78b67ed61e0",
"type": "AGENT_START"
},
'header': {
"version" : "1.0",
"exchange": "clound-agent",
"routingKey": "service.cmd",
"type": "SERVICE",
"content_type": "application/json",
"content_encoding": "utf-8",
"isSuccessful": True

},
"commands": [
"echo 0> /root/test-cww.txt"
]
}
print json.dumps(message)
channel.basic_publish(exchange='cloud-agent', routing_key='cc', body=json.dumps(message))

connection.close()
