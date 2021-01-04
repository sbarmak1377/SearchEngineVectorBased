from InvertedIndex import *
from Document import tokenizer


def query_handler(query: str, invertedIndex: InvertedIndex):
    number = len(query.split())
    if (number == 1):
        res = one_word_handler(query, invertedIndex)
        return invertedIndex.index_array[res]
    else:
        res = multi_word_handler(query, invertedIndex)
        return res


def one_word_handler(query: str, invertedIndex: InvertedIndex):
    res = binary_search(invertedIndex, 0, len(invertedIndex.index_array) - 1, query)
    return res


def multi_word_handler(query: str, invertedIndex: InvertedIndex):
    words = tokenizer(query)
    res = []
    for word in words:
        word_index = binary_search(invertedIndex, 0, len(invertedIndex.index_array) - 1, word)
        if word_index == -1:
            break
        for i in range(len(invertedIndex.index_array[word_index].doc_ids)):
            res_index = result_binary_search(res, 0, len(res) - 1, invertedIndex.index_array[word_index].doc_ids[i])
            if res_index == -1:
                res.append([invertedIndex.index_array[word_index].doc_ids[i], 1])
            else:
                res[res_index][1] += 1
    res = sorted(res)
    return res


def binary_search(invertedIndex: InvertedIndex, start, end, query):
    if end >= start:

        mid = int(start + (end - start) / 2)

        if invertedIndex.index_array[mid].word == query:
            return mid

        elif invertedIndex.index_array[mid].word > query:
            return binary_search(invertedIndex, start, mid - 1, query)

        else:
            return binary_search(invertedIndex, mid + 1, end, query)

    else:
        return -1


def result_binary_search(array, start, end, query):
    if end == 0:
        return -1

    if end >= start:

        mid = int(start + (end - start) / 2)
        if array[mid][0] == query:
            return mid

        elif array[mid][0] > query:
            return result_binary_search(array, start, mid - 1, query)

        else:
            return result_binary_search(array, mid + 1, end, query)

    else:
        return -1
