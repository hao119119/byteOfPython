import bottle
import yaml
import json
import service
import pymongo


@bottle.route('/')
def index():
    return 'hello_world'


@bottle.route('/oozie-service-broker/v2/catalog')
def catalog():
    f = open('settings.yml')
    data_map = yaml.load(f)
    print type(data_map)
    json_str = json.dumps(data_map)
    print json_str
    f.close()
    return json_str


@bottle.route('/oozie-service-broker/v2/service_instances/:instance_id', method='PUT')
def put_service_instance(instance_id):
    a = bottle.request.json
    a['instance_id'] = instance_id
    print a
    print type(a)
    print ' '.join([instance_id, 'put'])
    return a


@bottle.route('/oozie-service-broker/v2/service_instances/:instance_id', method='DELETE')
def delete_service_instance(instance_id):
    a = bottle.request.json
    print a
    print type(a)
    print ' '.join([instance_id, 'delete'])
    return {'a': 'abcd'}


@bottle.route('/oozie-service-broker/v2/service_instances/:instance_id/service_bindings/:id', method='PUT')
def create_bing(instance_id, id):
    a = bottle.request.json
    print a
    print ' '.join([instance_id, 'put'])


@bottle.route('/oozie-service-broker/v2/service_instances/:instance_id/service_bindings/:id', method='DELETE')
def remove_bing(instance_id, id):
    a = bottle.request.json
    print a
    print ' '.join([instance_id, 'delete'])

bottle.debug(True)
bottle.run(host='10.4.11.96', port=8082)

# command
# db.names.insert({ name:'chen hao'})
# db.names.insert({ name:'cc', age:16})
# var c = db.names.findOne({name:'cc'})
# c.age=18
# db.names.save(c)
