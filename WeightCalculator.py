from Document import *
import math


def idf(word: str, docs: list):
    docs_count = len(docs)
    word_doc_count = 0
    for i in range(len(docs)):
        if docs[i].words_dictionary.get(word):
            word_doc_count += 1
    if word_doc_count != 0:
        return math.log(len(docs) / word_doc_count, 10)
    else:
        return 0


def tf(word: str, doc: Document):
    temp = doc.words_dictionary.get(word)
    if temp is not None:
        return 1 + math.log(temp, 10)
    else:
        return 0


def weight_calculator_doc(word: str, docs, doc):
    doc_idf = idf(word, docs)
    word_doc_fr = tf(word, doc)
    if doc_idf < 0.3:
        return doc_idf * word_doc_fr
    else:
        return 0



