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




# get all deadlines from a user in which the type is equal to the input
#



# get all deadlines from a user sorted by title alphabetical 




# get all deadlines from a user sorted by due date




# get all deadlines from a user sorted by type




# get all deadlines from a user sorted by classname


