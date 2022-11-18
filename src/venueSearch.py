import sys
import json
from pymongo import MongoClient
import re


def findVenues(n, collection):
    # results = collection.find({"authors": "/" + keyword + "/"})
    results = collection.find({'venue':{'$regex':"international conference on computer vision and graphics"}})
    # results = collection.find({'venue': "international conference on computer vision and graphics"})
    retVal = []
    for venue in results:
        retVal.append({"names": venue["authors"]})
    return retVal

