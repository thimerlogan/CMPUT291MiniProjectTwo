import sys
import json
from pymongo.collection import Collection


def findAuthors(keyword, collection: Collection):
    # Partial Matching
    # results = collection.find({"authors": {'$regex':'(?i)^.*'+ keyword +'.*$'} })
    
    # Full word matching
    results = collection.find({"authors": {'$regex':'(?i)\\b'+ keyword +'\\b'} })
    
    authors: dict = {}
    for entry in results:
        for author in entry["authors"]:
            if (keyword.lower() in author.lower()):
                if (author in authors):
                    authors[author].append(entry)
                else:
                    authors[author] = [entry]
    return authors