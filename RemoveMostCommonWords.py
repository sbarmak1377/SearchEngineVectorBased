from InvertedIndex import *


def remove_common_words_with_known_words(index_array: InvertedIndex):
    known_words = ["از", "با", "به", "برای", "تا", "در", "که", "ازای", "یا", "پس", "اگر", "اما", "زیرا", "لکن", "لیکن",
                   "را", "نیز", "ولی", "هم", "بی", "بدون"]
    for x in known_words:
        index_array.remove_word(x)


def remove_common_words_from_query(query_array):
    known_words = ["از", "با", "به", "برای", "تا", "در", "که", "ازای", "یا", "پس", "اگر", "اما", "زیرا", "لکن", "لیکن",
                   "را", "نیز", "ولی", "هم", "بی", "بدون"]
    res = query_array
    for i in range(len(query_array)):
        for j in range(len(known_words)):
            if query_array[i] == known_words[j]:
                query_array.remove(i)
                break
    return res


def remove_most_used_words_from_indexes(inverted_array: InvertedIndex, number_to_remove: int):
    max = 0
    index = 0
    for remover in range(number_to_remove):
        for i in range(inverted_array.index_array):
            if len(inverted_array.index_array[i].docs_id) > max:
                max = len(inverted_array.index_array[i].docs_id)
                index = i
        inverted_array.index_array.remove(index)
    return
