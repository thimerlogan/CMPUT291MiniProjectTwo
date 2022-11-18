import sys
import json
from pymongo import MongoClient

db = None

def main(args):
    if len(args) < 2:
        print("Not enough command line arguments")
    
    port = args[1]
    
    # Connect to the port on localhost
    host = f"""mongodb://localhost:{port}"""
    client = MongoClient(host)

    # Create or open the 291db database on server.
    global db 
    db = client["291db"]

    collist = db.list_collection_names()
    print(collist)

    

if __name__ == "__main__":
    main(sys.argv)