from InvertedIndex import *


def query_handler(query: str, invertedIndex: InvertedIndex):
    number = len(query.split())
    if (number == 1):
        res = one_word_handler(query, invertedIndex)
    else:
        res = multi_word_handler(query, invertedIndex)
    return res


def one_word_handler(query: str, invertedIndex: InvertedIndex):
    res = binary_search(invertedIndex, 0, len(invertedIndex.index_array) - 1, query)
    return res


def multi_word_handler(query: str, invertedIndex: InvertedIndex):
    words = query.split()
    temp = []
    res = []
    for word in words:
        word_index = binary_search(invertedIndex, 0, len(invertedIndex.index_array), word)
        for i in range(len(invertedIndex.index_array[word_index].docs_id)):
            res_index = result_binary_search(res, 0, len(res), invertedIndex.index_array[word_index].docs_id[i])
            if res_index == -1:
                res.append([invertedIndex.index_array[word_index].docs_id[i], 1])
            else:
                res[res_index][1] += 1
    res = sorted(res)
    return res


def binary_search(invertedIndex: InvertedIndex, start, end, query):
    if end >= start:

        mid = start + (end - start) / 2

        if invertedIndex.index_array[mid].word == query:
            return mid

        elif invertedIndex.index_array[mid].word > query:
            return binary_search(invertedIndex, start, mid - 1, query)

        else:
            return binary_search(invertedIndex, mid + 1, end, query)

    else:
        return -1


def result_binary_search(array, start, end, query):
    if end >= start:

        mid = start + (end - start) / 2

        if array[mid][0] == query:
            return mid

        elif array[mid][0] > query:
            return binary_search(array, start, mid - 1, query)

        else:
            return binary_search(array, mid + 1, end, query)

    else:
        return -1
