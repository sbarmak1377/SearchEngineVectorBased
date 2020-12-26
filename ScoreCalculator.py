import Document
import InvertedIndex
import WeightCalculator


def score_calculator(invertedIndex: InvertedIndex, docs, query, k):
    query_doc = Document.Document(query, 1)
    query_score = query_score_calculator(query_doc, docs)
    query_words = query_doc.words
    index_res = []
    for i in range(len(query_words)):
        loc = invertedIndex.find_word(query_words[i])
        if loc == -1:
            print("word " + query_words[i] + " can't be found in List!")
        else:
            index_res.append(invertedIndex.index_array[loc])
    docs_score = docs_score_calculator(index_res, docs)


def docs_score_calculator(indexes, docs):
    res = []
    for i in range(len(indexes)):
        word = indexes[i].word
        word_docs = indexes[i].doc_ids
        temp_res = [word]
        for j in range(len(word_docs)):
            id_location = Document.documents_binary_search(docs, 0, len(docs) - 1, word_docs[j])
            weight = WeightCalculator.weight_calculator_doc(word, docs, docs[id_location])
            temp_res.append([word_docs[j], weight])
        res.append(temp_res)
    return res


def query_score_calculator(doc: Document.Document, docs):
    res = []
    words = doc.words
    for i in range(len(words)):
        weight = WeightCalculator.weight_calculator_doc(words[i], docs, doc)
        res.append([words[i], weight])
    return res
