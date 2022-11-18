import sys
import json
from pymongo import MongoClient
import authorSearch
import venueSearch

def printMenu():
    print("""
1 - Search For Artists
2 - Search for authors
3 - List the venues
4 - Add an article
5 - Exit
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
    db = client["291db"]
    collection = db['dblp']

    ### MENU AREA ###
    printMenu()
    while True:
        userInput = int(getInput("", "Must make a selection"))
        if userInput == 1:
            return True
            
        elif userInput == 2:
            keyword = getInput("Author Name: ", "Must make a selection")
            authors = authorSearch.findAuthors(keyword, collection)
            print (authors)
           
        elif userInput == 3:
            n = int(getInput("Number of Venues: ", "Must make a selection"))
            venues = venueSearch.findVenues(n, collection)
            print(venues)
           
        elif userInput == 4:
            return True
        elif userInput == 5:
            return True
        else:
            print("Refer to menu")

    

if __name__ == "__main__":
    main(sys.argv)