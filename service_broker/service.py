import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.service_broker
service = db.service


def insert(info):
    service.insert_one(info)


def delete_service_instance(instance_id):
    pass


def delete_service_binding(instance_id, id):
    pass
