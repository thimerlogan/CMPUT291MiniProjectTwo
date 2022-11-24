

import sys
import json
from pymongo import MongoClient
import re


def findVenues(n, collection, db, client):
    client.admin.command({'setParameter': 1, 'internalQueryForceClassicEngine': True });
    results = collection.aggregate([
        {'$group' :
            {'_id': 
                {'venue': "$venue"},
            'ids' : 
                {'$addToSet': "$id"},          
            'venCount':
                {'$sum' : 1}
            }
        },
        {
            '$lookup': {
                'from': 'dblp',
                'localField': 'ids',
                'foreignField': 'references',
                'as': "combined"
            }
        },
        {"$sort": 
            { "combined" : -1, "venCount": -1 },
        },
        # {'$merge' : { 'into': { 'coll': "venue_merge" }, 'on': ['_id'],  'whenMatched': "replace", 'whenNotMatched': "insert" } }
    ])
    client.admin.command({'setParameter': 1, 'internalQueryForceClassicEngine': False });
          

    return results
