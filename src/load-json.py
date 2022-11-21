import sys
import json
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

    # Create or open the 291db database on server.
    db = client["291db"]

    # Create or open the collection in the db
    dblp = db["dblp"]

    # delete all previous entries in the dblp collection
    # specify no condition.
    dblp.delete_many({})
    dblp.drop_indexes()

    with open(filename) as f:
        for line in f:
            data = json.loads(line)
            data["year"] = str(data["year"])
            dblp.insert_one(data)

    dblp.create_index([('title', TEXT), ('authors', TEXT), ('abstract', TEXT), ('venue', TEXT), ('year', TEXT)], default_language="none")
    

    client.close()
    

if __name__ == "__main__":
    main(sys.argv)