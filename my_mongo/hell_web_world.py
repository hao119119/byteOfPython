import bottle
import pymongo

@bottle.route('/')
def index():

    # connect to mongoDB
    connection = pymongo.MongoClient('localhost', 27017)

    db = connection.test

    names = db.names
    #
    item = names.find_one()

    return '<b>Hello %s!<b>' % item['name']

bottle.run(host='localhost', port=8082)

# command
# db.names.insert({ name:'chen hao'})
# db.names.insert({ name:'cc', age:16})
# var c = db.names.findOne({name:'cc'})
# c.age=18
# db.names.save(c)
