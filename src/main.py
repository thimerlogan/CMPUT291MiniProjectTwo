import sys
import json
from pymongo import MongoClient
import authorSearch
import venueSearch
import articleSearch
import addArticle

def printMenu():
    print("""
1 - Search for articles
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
    
    while True:
        printMenu()
        userInput = int(getInput("", "Must make a selection"))
        if userInput == 1:
            keywords = getInput("Article search keywords: ", "Must make a selection")
            articles = articleSearch.searchForArticles(keywords.split(), collection)

            if len(list(articles.clone())) < 1:
                print("\nThere were no matching articles")
                continue

            articlesDict = dict((i, article) for i, article in enumerate(articles, 1))
            print(f"\nThere were {articlesDict.__len__()} search results:")   
            print("   | id | title | year | venue |")
            for i, article in articlesDict.items():
                print(f"{i}. {article['id']} | {article['title']} | {article['year']} | {article['venue']} ")
            
            print(f"{len(articlesDict) + 1}. back")
            selection = int(getInput("\nSelect an article: ", "Must make a selection"))
            while selection < 1 and selection > (len(articlesDict) + 1):
                print("Invalid selection")
                selection = int(getInput("Select an article: ", "Must make a selection"))
            
            if selection == (len(articlesDict) + 1):
                continue

            articleSearch.printArticle(articlesDict[selection], collection)       

            
        elif userInput == 2:
            keyword = getInput("Author Name: ", "Must make a selection")
            authors = authorSearch.findAuthors(keyword, collection)
            
            count: int = 1
            selectionDict: dict = {}
            for key, value in authors.items():
                selectionDict[count] = key
                print(count, '|' , key,'|', len(value))
                count = count + 1
            print(count + 1, "| Exit")
                
            n = int(getInput("Author: ", "Must make a selection"))
            if(n == count + 1):
                continue
            
            
            selected = sorted(authors[selectionDict[n]], key=lambda d: d['year'], reverse=True) 
            for publication in selected:
                print(publication["title"], '|', publication["year"], '|', publication["venue"])
                
        elif userInput == 3:
            n = int(getInput("Number of Venues: ", "Must make a selection"))
            venues = venueSearch.findVenues(n, collection, db, client)
            i = 0
            for venue in venues:
                if (i == n):
                    continue
                
                if (venue['_id']['venue'] != ""):    
                    print(venue['_id']['venue'], "| Count -", venue['venCount'], "| RefCount -" , len(venue['combined']))
                    i = i + 1
           
           
        elif userInput == 4:
            uniqueId = getInput("Enter a unique ID: ", "Must enter a unique ID")
            while not addArticle.isArticleIdUnique(uniqueId, collection):
                print("Article ID is not unique")
                uniqueId = getInput("Enter a unique ID: ", "Must enter a unique ID")

            title = getInput("Enter a title: ", "Must enter a title")
            authors = getInput("Enter authors (comma separated): ", "Must enter an author").split(',')
            authors = list(map(str.strip, authors))
            year = getInput("Enter a year: ", "Must enter a year")
            addArticle.addArticle(uniqueId, title, authors, year, collection)

            print("\nArticle added!")

        elif userInput == 5:
            return True
        else:
            print("Refer to menu")

    

if __name__ == "__main__":
    main(sys.argv)