import os
from typing import List
import Document


def getAllDocuments():
    files = os.listdir("./Docs")
    for i in range(len(files)):
        files[i] = "./Docs/" + files[i]
    docs: List[Document.Document] = []
    for single_file in files:
        x = Document.Document(single_file, 0)
        docs.append(x)
    docs = sorted(docs)
    return docs


if __name__ == '__main__':
    a = getAllDocuments()
    for x in a:
        print(x.doc_id)
