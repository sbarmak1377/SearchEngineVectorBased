import Document
import FetchDocument
import InvertedIndex
import SimpleQueryhandler

if __name__ == '__main__':
    docs = FetchDocument.getAllDocuments()
    inverted_index = InvertedIndex.InvertedIndex()
    for i in range(len(docs)):
        for j in range(len(docs[i].words)):
            inverted_index.add_id(docs[i].words[j], docs[i].doc_id)
    inverted_index.print_all()
    query = input("Please Enter your Query:\n")
    res = []
    res.append(SimpleQueryhandler.query_handler(query, inverted_index))
    print(res)