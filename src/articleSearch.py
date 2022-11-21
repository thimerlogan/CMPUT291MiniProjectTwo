from pymongo.collection import Collection

def searchForArticles(keywords:list, collection:Collection):
    regex = "^"
    words = ""
    for keyword in keywords:
        words += f"\"{keyword}\" "
        regex += f"(?=.*{keyword})"

    #results = collection.find({"$or": [{"authors": { "$elemMatch": { "$regex": regex, "$options": 'i' }}}, {"title": { "$regex": regex, "$options": 'i' }}, 
    #                        {"abstract": { "$regex": regex, "$options": 'i' }}, {"venue": { "$regex": regex, "$options": 'i' }}]})
    #results = collection.find({"$text": {"$search": ' '.join(map(str, keywords))}})
    results = collection.find({"$text": {"$search": words}})
    return results

def getArticles(ids:list, collection:Collection):
    print(f"ids: {ids}")
    results = collection.find({"id": {"$in": ids}})
    print(f"results: {len(list(results.clone()))}")

    return results

def printArticle(article, collection:Collection):
    print(f"\nid: {article['id']}")
    print(f"title: {article['title']}")
    print(f"year: {article['year']}")
    print(f"venue: {article['venue']}")
    print(f"# of citations: {article['n_citation']}")
    print(f"authors: {', '.join(map(str, article['authors']))}")

    # some don't have an abstract key
    try:
        print(f"abstract: {article['abstract']}")
    except KeyError:
        print("abstract: ")
    
    # some don't have an abstract key
    try:
        print(f"references: {', '.join(map(str, article['references']))}")

    except KeyError:
        print("references: ")
    

