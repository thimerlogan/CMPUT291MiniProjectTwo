import sys
import json
from pymongo import MongoClient


def findAuthors(keyword, collection):
    # results = collection.find({"authors": "/" + keyword + "/"})
    results = collection.find({"authors": { "$elemMatch": { "$regex": "/.*" + keyword +".*/" }}})
    retVal = []
    for author in results:
        retVal.append({"names": author["authors"]})
    return retVal

