import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.school
scores = db.scores


def find():
    # sort, skip, limit in order
    print 'find, reporting for duty'
    query = {}
    try:
        # cursor = scores.find(query).sort('student_id', pymongo.ASCENDING).skip(4).limit(1)
        cursor = scores.find(query).sort([('student_id', pymongo.ASCENDING), ('score', pymongo.DESCENDING)])
    except Exception as e:
        print 'error', type(e), e
    for doc in cursor:
        print doc

find()