from pymongo.collection import Collection

def searchForArticles(keywords:list, collection:Collection):
    #regex = "^"
    words = ""
    for keyword in keywords:
        words += f"\"{keyword}\" "
        #regex += f"(?=.*{keyword})"
    
    results = collection.find({"$text": {"$search": words}})

    return results

def getArticlesThatReference(id, collection:Collection):
    results = collection.find({"references": id})

    return results
    

def printArticle(article, collection:Collection):
    print(f"\nid: {getArticleKey(article, 'id')}")
    print(f"title: {getArticleKey(article, 'title')}")
    print(f"year: {getArticleKey(article, 'year')}")
    print(f"venue: {getArticleKey(article, 'venue')}")
    print(f"# of citations: {getArticleKey(article, 'n_citation')}")
    print(f"authors: {', '.join(map(str, getArticleKey(article, 'authors')))}")
    print(f"abstract: {getArticleKey(article, 'abstract')}")

    if getArticleKey(article, 'references') == 'None':
        print("references: None")
    else:
        print(f"references: {', '.join(map(str, getArticleKey(article, 'references')))}")
    
    articleReferences = getArticlesThatReference(getArticleKey(article, 'id'), collection)
    print("Articles that reference this one: ")
    if len(list(articleReferences.clone())) < 1:
        print("None")
        return
    
    print("\t| id | title | year")
    for article in articleReferences:
        print(f"\t{article['id']} | {article['title']} | {article['year']}")

    
def getArticleKey(article, key:str):
    try:
        return article[key]
    except KeyError:
        return 'None'
