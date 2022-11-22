from pymongo.collection import Collection

def addArticle(uniqueId:str, title:str, authors:list, year:str, collection:Collection):
    doc = {
            "id": uniqueId,
            "title": title,
            "authors": authors, 
            "year": year,
            "n_citations": 0, 
            "abstract": None,
            "venue": None, 
            "references": list()}
    
    collection.insert_one(doc)

    return

def isArticleIdUnique(id:str, collection:Collection) -> bool:
    return collection.count_documents({"id": id}) == 0