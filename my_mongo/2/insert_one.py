# insert_one
# insert_many
# update_one
# update_many
# replace_one
# delete_one

import pymongo
import sys

# establish a connection to the databse
connection = pymongo.MongoClient('mongodb://localhost')


def insert():
    # get a handle to the school data
    db = connection.school
    people = db.people

    print 'insert, reporting for duty'

    richard = {"name": "Richard Kreuter", "company": "10gen",
               "interests": ['horese', 'skydiving', 'fencing']}
    andrew = {"_id": "erlichson", "name": "Andrew Erlichson", "company": "10gen",
              "interests": ['running', 'cycling', 'photography']}

    try:
        people.insert_one(richard)
        print richard
        people.insert_one(andrew)
    except Exception as e:
        print 'error', type(e), e


def insert_many():
    db = connection.school
    people = db.people
    richard = {"name": "Richard Kreuter", "company": "10gen",
               "interests": ['horese', 'skydiving', 'fencing']}
    andrew = {"_id": "erlichson", "name": "Andrew Erlichson", "company": "10gen",
              "interests": ['running', 'cycling', 'photography']}
    people_to_insert = [andrew, richard]

    try:
        people.insert_many(people_to_insert, ordered=True)
    except Exception as e:
        print 'error', type(e), e

# insert()
insert_many()
