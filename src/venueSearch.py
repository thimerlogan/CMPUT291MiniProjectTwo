

import sys
import json
from pymongo import MongoClient
import re


def findVenues(n, collection, db, client):
    # Grabs venues with the most articles
    # results = collection.aggregate([
    #     {'$group' :
    #         {'_id': 
    #             {'venue': "$venue"},
    #         'name' : 
    #             {'$addToSet': '$id' },
    #         'venCount':
    #             {'$sum' : 1}
    #         }
    #     }, 
    #     {"$sort": 
    #         { "venCount" : -1 }
    #     }
    # ])
    
    
    
    
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
                'foreignField': 'refernces',
                'as': 'combined'
            }
        },
        {"$sort": 
            { "venCount" : 1 }
        },
        # {'$merge' : { 'into': { 'coll': "venue_merge" }, 'on': ['_id'],  'whenMatched': "replace", 'whenNotMatched': "insert" } }
    ])
    
    
    

    
    # results = collection.find({'references': {'$nin': ['']}})
    
                    # {'$addToSet': '$id' },
    
    # print(list(results[1:100]))

    # results = db.collection['venue_merge'].find({})
    # print(list(results))
    for document in results:
        if (document['_id']['venue'] == "Journal of Automata, Languages and Combinatorics"):
            print(document)
          
    # print(list(results)[0:100])
    
    # count = 0
    # for venue in results:
    #     if (count == n):
    #         continue
        
    #     if venue["_id"]["venue"] != "":
    #         collection.find()
            
    #         print(venue["_id"]["venue"], "|", venue["venCount"], venue["name"])
    #         count = count + 1
    
    
    
    # results = collection.distinct('venue')
    # venueCount = {}
    # for venue in results: 
    #     if venue != '':
    #         selectedVenues = (collection.find({"venue": venue}))
           
    #         # Get the ids of the venue and count references
    #         ids = []
    #         for venueselc in selectedVenues:
    #             ids.append(venueselc["id"])
                
    #         print(ids)    
    #         references = collection.find({"references" : {"$in": ids}})
    #         # print(len(list(references)))
            
        
    #         venueCount[venue] = {"articleCount": len(list(selectedVenues)), "refCount": len(list(references))}

    # print(venueCount)
    return results




    # results = collection.aggregate([
    #     {'$group' :
    #         {'_id': 
    #             {'venue': "$venue"},
    #         'name' : 
    #             {'$addToSet': '$id' },
    #         'venCount':
    #             {'$sum' : 1}
    #         }
    #     }, 
    #     {"$sort": 
    #         { "venCount" : -1 }
    #     }
    # ])
    # # print(list(results)[0:100])
    
    # count = 0
    # for venue in results:
    #     if (count == n):
    #         continue
        
    #     if venue["_id"]["venue"] != "":
    #         collection.find()
            
    #         print(venue["_id"]["venue"], "|", venue["venCount"], venue["name"])
    #         count = count + 1