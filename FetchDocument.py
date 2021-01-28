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


def getAllDocuments2():
    files = os.listdir("./Docs2")
    for i in range(len(files)):
        files[i] = "./Docs2/" + files[i]
    docs: List[Document.Document] = []
    for single_file in files:
        x = Document.Document(single_file, 0)
        docs.append(x)
    docs = sorted(docs)
    return docs


def getMathDocuments():
    files = os.listdir("./Docs3/Math")
    for i in range(len(files)):
        files[i] = "./Docs3/Math/" + files[i]
    docs: List[Document.Document] = []
    for single_file in files:
        x = Document.Document(single_file, 0)
        docs.append(x)
    docs = sorted(docs)
    return docs


def getHealthDocuments():
    files = os.listdir("./Docs3/Health")
    for i in range(len(files)):
        files[i] = "./Docs3/Health/" + files[i]
    docs: List[Document.Document] = []
    for single_file in files:
        x = Document.Document(single_file, 0)
        docs.append(x)
    docs = sorted(docs)
    return docs


def getHistoryDocuments():
    files = os.listdir("./Docs3/History")
    for i in range(len(files)):
        files[i] = "./Docs3/History/" + files[i]
    docs: List[Document.Document] = []
    for single_file in files:
        x = Document.Document(single_file, 0)
        docs.append(x)
    docs = sorted(docs)
    return docs


def getPhysicsDocuments():
    files = os.listdir("./Docs3/Physics")
    for i in range(len(files)):
        files[i] = "./Docs3/Physics/" + files[i]
    docs: List[Document.Document] = []
    for single_file in files:
        x = Document.Document(single_file, 0)
        docs.append(x)
    docs = sorted(docs)
    return docs


def getTechDocuments():
    files = os.listdir("./Docs3/Technology")
    for i in range(len(files)):
        files[i] = "./Docs3/Technology/" + files[i]
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
