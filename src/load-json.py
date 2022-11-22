import sys
import os
from pymongo import MongoClient
from pymongo import TEXT

def main(args):
    if len(args) < 3:
        print("Not enough command line arguments")
        return
    
    port = args[2]
    filename = args[1]

    
    
    # Connect to the port on localhost
    host = f"""mongodb://localhost:{port}"""
    client = MongoClient(host)

    os.system(f'mongoimport -d 291db -c dblp --drop --file {filename}')

    # Create or open the 291db database on server.
    db = client["291db"]

    # Create or open the collection in the db
    dblp = db["dblp"]

    dblp.drop_indexes()

    # change the year field to a string so we can use it in the text index
    print("Updating year fields to strings")
    dblp.update_many({}, [{"$set": {"year": {"$toString": "$year"}}}])
    print("Done updating year fields to strings")

    print("Creating text indexes")
    dblp.create_index([('title', TEXT), ('authors', TEXT), ('abstract', TEXT), ('venue', TEXT), ('year', TEXT)], default_language="english")
    print("Done creating text indexes")
    

    client.close()
    

if __name__ == "__main__":
    main(sys.argv)