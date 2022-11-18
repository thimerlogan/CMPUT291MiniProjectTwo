import sys
import json
from pymongo import MongoClient

db = None

def printMenu():
    print("""
1 - Search For Artists
2 - Search for authors
3 - List the venues
4 - Add an article
Enter a choice and press enter:""")

def getInput(message, errMessage):
    while True:
        toRet = input(message)
        if (toRet == ""):
            print(errMessage)
        else:
            return toRet

    return

def main(args):
    ### CONNECTION AREA ###
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


    ### MENU AREA ###
    printMenu()
    while True:
        userInput = int(getInput("", "Must make a selection"))
        if userInput == 1:
            return True
        elif userInput == 3:
            return True
        elif userInput == 3:
            return True
        elif userInput == 4:
            return False
        else:
            print("Refer to menu")

    

if __name__ == "__main__":
    main(sys.argv)