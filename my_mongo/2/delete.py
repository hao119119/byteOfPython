import pymongo
import sys

# establish a connection to the databse
connection = pymongo.MongoClient('mongodb://localhost')


# remove one student
def remove_student(student_id):
    # get a handle to the school database
    db = connection.school
    scores = db.scores

    try:
        # result = scores.delete_one({'student': student_id})
        result = scores.delete_many({'student': student_id})
        print 'num removed: ', result.deleted_count
    except Exception as e:
        print 'Exception ', type(e), e


def find_student_data(student_id):
    db = connection.school
    scores = db.scores

    try:
        docs = scores.find({'student': student_id})
        for doc in docs:
            print doc
    except Exception as e:
        print 'error: ', type(e), e

remove_student(1)
find_student_data(1)
