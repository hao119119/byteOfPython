import pymongo
import sys


connection = pymongo.MongoClient("mongodb://localhost")
db = connection.school
scores = db.scores


def find():
    print 'find, reporting for duty'
    query = {'type': 'exam'}
    try:
        cursor = scores.find(query)
    except Exception as e:
        print "Unexpected error:", type(e), e
    sanity = 1
    for doc in cursor:
        print doc
        sanity += 1
        if sanity > 10:
            break


def find_one():
    print 'find one, reporting for duty'
    query = {'student': 10}
    try:
        doc = scores.find_one(query)
    except Exception as e:
        print "Unexpected error:", type(e), e
    print doc


def find_projection():
    query = {'type': 'exam'}
    projection = {'student': 1, '_id': 0}

    try:
        cursor = scores.find(query, projection)
    except Exception as e:
        print "error", type(e), e

    for doc in cursor:
        print doc


def find_gt():
    query = {'type': 'exam', 'score': {'$gt': 50, '$lt': 70}}
    projection = {'student': 1, '_id': 0, 'score': 1}
    try:
        cursor = scores.find(query, projection)
    except Exception as e:
        print "error", type(e), e
    for doc in cursor:
        print doc
#
# find_one()
#
# find()
#
# find_projection()

find_gt()