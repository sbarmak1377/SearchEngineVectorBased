import os
from Document import *


def getAllDocuments():
    files = os.listdir("./Docs")
    for i in range(len(files)):
        files[i] = "./Docs/" + files[i]
    docs = []
    for single_file in files:
        docs.append(Document(single_file, 0))
    docs = sorted(docs)
    return docs


if __name__ == '__main__':
    a = getAllDocuments()
    for x in a:
        print(x.doc_id)
