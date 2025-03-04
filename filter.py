'''
This file contains custom helper functions necessary to sort and filter data from the MongoDB database

These functions are intended to be called by the main Flask application (app.py) and returned to it for use
'''
#import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId
#import datetime
import database


# get all deadlines from a user in which the title contains a search string
# example: input s="Problem Set" should return the deadlines titled "Problem Set 1" and "problem set 2"
# case INsensitive (capitalization does not matter)
def search_similar_deadline(mydb, userID, name):
    usertable = mydb["Deadline"]

    my_deadlines = usertable.find({
        "user_ID" : ObjectId(userID),
        "name": {"$regex": name, "$options": "i"}
    })

    return list(my_deadlines)




# get all deadlines from a user in which the type is equal to the input
#
def search_exact_deadline(mydb, userID, dtype):
    usertable = mydb["Deadline"]

    my_deadlines = usertable.find({
        "user_ID" : ObjectId(userID),
        "type": dtype
    })

    return list(my_deadlines)


# get all deadlines from a user sorted by title alphabetical 
def search_sort_alpha_deadline(mydb, userID):
    usertable = mydb["Deadline"]

    my_deadlines = usertable.find({
        "user_ID" : ObjectId(userID)
    })

    my_deadlines.sort("name", 1)

    return list(my_deadlines)



# get all deadlines from a user sorted by due date
def search_sort_date_deadline(mydb, userID):
    usertable = mydb["Deadline"]

    my_deadlines = usertable.find({
        "user_ID" : ObjectId(userID)
    }).sort("due_date", 1)

    return list(my_deadlines)



# get all deadlines from a user sorted by type
def search_sort_type_deadline(mydb, userID):
    usertable = mydb["Deadline"]

    my_deadlines = usertable.find({
        "user_ID" : ObjectId(userID)
    })

    my_deadlines.sort("type", 1)

    return list(my_deadlines)



# get all deadlines from a user sorted by classname
def search_sort_class_deadline(mydb, userID):
    usertable = mydb["Deadline"]

    my_deadlines = usertable.find({
        "user_ID" : ObjectId(userID)
    })

    my_deadlines.sort("class_ID", 1)

    return list(my_deadlines)

