import math
import os

import FetchDocument
import MaxHeap
import ScoreCalculator
import CosinusCalculator
import Document
import WeightCalculator


def getAllDocuments():
    files = os.listdir("./Docs")
    for i in range(len(files)):
        files[i] = "./Docs/" + files[i]
    docs = []
    for single_file in files:
        docs.append(Document(single_file))
    docs = sorted(docs)
    return docs


if __name__ == '__main__':
    a = getAllDocuments()
    for x in a:
        print(x.doc_id)


class Index:
    word = ""
    doc_ids = []

    def __init__(self, word):
        self.word = word

    def add_id(self, doc_id):
        self.doc_ids.append(doc_id)
        self.doc_ids = sorted(self.doc_ids)

    def insert_id(self, position, doc_id):
        self.doc_ids.insert(position, doc_id)
        self.doc_ids = sorted(self.doc_ids)

    def remove_id(self, doc_id):
        for i in range(len(self.doc_ids)):
            if doc_id == self.doc_ids[i]:
                self.doc_ids.remove(i)

    def find_location(self, doc_id):
        for i in range(len(self.doc_ids)):
            if self.doc_ids[i] > doc_id:
                return i
        return -1

    def check_id(self, doc_id):
        for i in range(len(self.doc_ids)):
            if self.doc_ids[i] == doc_id:
                return i
        return -1

    def __eq__(self, other):
        return self.word == other.word and len(self.doc_ids) == len(other.doc_ids)

    def __lt__(self, other):
        return self.word < other.word


class InvertedIndex:

    def __init__(self):
        self.index_array = []

    def remove_word(self, word):
        for i in range(len(self.index_array)):
            if self.index_array[i].word == word:
                self.index_array.remove(i)
                return

    def find_word(self, word):
        for i in range(len(self.index_array)):
            if self.index_array[i] == word:
                return i
        return -1

    def add_word(self, word):
        if self.find_word(word) >= 0:
            self.index_array.append(Index(word))
            self.index_array = sorted(self.index_array)
            return True
        return False

    def add_id(self, word, doc_id):
        ind = self.find_word(word)
        if ind < 0:
            self.add_word(word)
            word_loc = self.find_word(word)
            if word_loc < 0:
                return False
            if doc_id not in self.index_array[word_loc].doc_ids:
                self.index_array[word_loc].add_id(doc_id)
                return True
        else:
            if doc_id not in self.index_array[ind].doc_ids:
                self.index_array[ind].add - id(doc_id)
                return True

    def remove_id(self, word, doc_id):
        ind = self.find_word(word)
        if ind < 0:
            return False
        else:
            id_loc = self.index_array[ind].find_location(doc_id)
            if id_loc < 0:
                return False
            else:
                self.index_array[ind].remove_id(id_loc)
                return True


def remove_tar(word):
    if len(word) < 2:
        return word
    if len(word) > 2 and word[-2:] == "تر":
        return word[:-2]
    return word


def remove_tarin(word):
    if len(word) < 4:
        return word
    if len(word) > 4 and word[-4:] == "ترین":
        return word[:-4]
    return word


def remove_nim_fasele(word):
    if len(word) < 1:
        return word
    if word[-1] == "\u200c":
        return word[:-1]
    return word


def remove_on(word):
    if len(word) < 2:
        return word
    if len(word) > 2 and word[-2:] == "ان":
        return word[:-2]
    return word


def check_gan(word):
    single_word = word[:-3] + "ه"
    if single_word[-3:] == "نده":
        return True
    else:
        return False


def remove_gan(word):
    if len(word) < 3:
        return word
    if len(word) > 3 and word[-3:] == "گان" and check_gan(word):
        return word[:-3] + "ه"
    return word


def remove_ha(word):
    if len(word) < 2:
        return word
    if len(word) > 2 and word[-2:] == "ها":
        return word[:-2]
    return word


def remove_extends(word):
    word = remove_nim_fasele(word)
    word = remove_ha(word)
    word = remove_nim_fasele(word)
    word = remove_tarin(word)
    word = remove_nim_fasele(word)
    word = remove_tar(word)
    word = remove_nim_fasele(word)
    word_size = len(word)
    word = remove_gan(word)
    word_size2 = len(word)
    if word_size == word_size2 and word[-3:] == "گان":
        return word
    word = remove_nim_fasele(word)
    word = remove_on(word)
    word = remove_nim_fasele(word)
    return word


if __name__ == '__main__':
    word = "درختان"
    print(remove_extends(word))


def remove_common_words_with_known_words(index_array: InvertedIndex):
    known_words = ["از", "با", "به", "برای", "تا", "در", "که", "ازای", "یا", "پس", "اگر", "اما", "زیرا", "لکن", "لیکن",
                   "را", "نیز", "ولی", "هم"]
    for x in known_words:
        index_array.remove_word(x)


def remove_most_used_words_from_indexes(inverted_array: InvertedIndex, number_to_remove: int):
    max = 0
    index = 0
    for remover in range(number_to_remove):
        for i in range(inverted_array):
            if len(inverted_array.index_array[i].docs_id) > max:
                max = len(inverted_array.index_array[i].docs_id)
                index = i
        inverted_array.index_array.remove(index)
    return


def tokenizer(text):
    tokenized_string = text.split()
    for i in range(len(tokenized_string)):
        tokenized_string[i] = remove_ending(tokenized_string[i])
    return tokenized_string


def remove_ending(string):
    string = string.replace(".", "")
    string = string.replace("?", "")
    string = string.replace("!", "")
    string = string.replace("*", "")
    string = string.replace(")", "")
    string = string.replace("(", "")
    string = string.replace("<", "")
    string = string.replace(">", "")
    return string


class Document:
    word_count = 0
    doc_id = -1
    words = []

    def __init__(self, path):
        self.doc_id = int(path.split("/")[-1][:-4])
        lines = file_reader(path)
        for x in lines:
            new_words = tokenizer(x)
            self.word_count += len(new_words)
            for y in new_words:
                self.words.append(y)

    def __eq__(self, other):
        if self.doc_id == other.doc_id and self.word_count == other.word_count:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.doc_id < other.doc_id


if __name__ == '__main__':
    path = "Docs/6.txt"
    a = Document(path)
    print(a.doc_id)
    print(a.word_count)
    print(a.words)


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



class CosinusHelper:
    id = -1
    words = []
    weights = []

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id


class CosinusArray:
    helper_array = []

    def __init__(self, query_res, docs_res):
        temp = CosinusHelper()
        # print(query_res)
        # print(docs_res)
        for i in range(len(query_res)):
            temp.words.append(query_res[i][0])
            temp.weights.append(query_res[i][1])
        self.helper_array.append(temp)

        for i in range(len(docs_res)):
            arr = docs_res[i][1:]
            word = docs_res[i][0]
            temp = CosinusHelper()
            for j in range(len(arr)):
                index = find_index_cosinus_helper(self.helper_array, arr[j][0])
                if index == -1:
                    temp.id = arr[j][0]
                    temp.words.append(word)
                    temp.weights.append(arr[j][1])
                else:
                    self.helper_array[index].words.append(word)
                    self.helper_array[index].weights.append(arr[j][1])
        self.helper_array = sorted(self.helper_array)


def find_index_cosinus_helper(arr, doc_id):
    for i in range(len(arr)):
        if arr[i].id == doc_id:
            return i
    return -1


def single_cosinus_score(helper1: CosinusHelper, helper2: CosinusHelper):
    sum1 = 0
    sum2 = 0
    for i in range(len(helper1.weights)):
        sum1 += math.pow(helper1.weights[i], 2)
    for i in range(len(helper2.weights)):
        sum2 += math.pow(helper2.weights[i], 2)
    length1 = math.pow(sum1, 1 / 2)
    length2 = math.pow(sum2, 1 / 2)
    if length1 == 0 or length2 == 0:
        return 0
    score_sum = 0
    for i in range(len(helper1.words)):
        for j in range(len(helper2.words)):
            if helper1.words[i] == helper2.words[j]:
                score_sum += helper1.weights[i] * helper2.weights[j]
                break
    return score_sum / (length1 * length2)


# uses Above Class to perform better in creating max heap
def cosinus_max_heap_creator(query_res, docs_res):
    helper = CosinusArray(query_res, docs_res)
    score_final_result = []
    i = 1
    while i < len(helper.helper_array):
        score_final_result.append(
            [helper.helper_array[i].id, single_cosinus_score(helper.helper_array[0], helper.helper_array[i])])
    max_heap = MaxHeap.MaxHeap()
    for i in range(len(score_final_result)):
        max_heap.push(score_final_result[i])
    return max_heap

def score_calculator(invertedIndex: InvertedIndex, docs, query, k):
    query_doc = Document.Document(query, 1)
    query_score = ScoreCalculator.query_score_calculator(query_doc, docs)
    query_words = query_doc.words
    query_words = sorted(query_words)
    index_res = []
    for i in range(len(query_words)):
        loc = invertedIndex.find_word(query_words[i])
        if loc == -1:
            print("word " + query_words[i] + " can't be found in List!")
        else:
            index_res.append(invertedIndex.index_array[loc])
    docs_score = docs_score_calculator(index_res, docs)
    max_heap = CosinusCalculator.cosinus_max_heap_creator(query_score, docs_score)
    res = []
    if len(max_heap.heap) > 1 and len(max_heap.heap) > k:
        for i in range(k):
            res.append(max_heap.pop())
    elif 1 < len(max_heap.heap) < k + 1:
        for i in range(len(max_heap.heap)):
            res.append(max_heap.pop())
    return res


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

def file_reader(path):
    file = open(path, "r", encoding="utf-8")
    lines = []
    line = file.readline()
    while line:
        lines.append(line)
        line = file.readline()
    return lines



def calculate_centroid(inverted_index: InvertedIndex.InvertedIndex, docs):
    result = list()
    size = len(inverted_index.index_array)
    index_array = inverted_index.index_array
    docs_score = ScoreCalculator.docs_score_calculator(index_array, docs)
    for i in range(len(docs_score)):
        weights_sum = 0
        for j in range(1, len(docs_score[i])):
            weights_sum += docs_score[i][j][1]
        result.append(weights_sum / size)
    return result, docs_score


def find_best_cluster_index(inverted_indexes, centroids, query_scores):
    max_index = 0
    max_score = -1
    centroid_helpers = list()
    query_helpers = list()
    for i in range(len(centroids)):
        helper = CosinusCalculator.CosinusHelper()
        for j in range(len(inverted_indexes[i].index_array)):
            helper.words.append(inverted_indexes[i].index_array[j])
            helper.weights.append(centroids[i][j])
        centroid_helpers.append(helper)
    for i in range(len(query_scores)):
        helper = CosinusCalculator.CosinusHelper()
        for j in range(len(query_scores[i])):
            helper.words.append(query_scores[i][j][0])
            helper.weights.append(query_scores[i][j][1])
        query_helpers.append(helper)
    for i in range(len(centroids)):
        score = CosinusCalculator.single_cosinus_score(centroid_helpers[i], query_helpers[i])
        if score > max_score:
            max_score = score
            max_index = i
    return max_index


if __name__ == '__main__':
    # We are Processing in Alphabet Doc Category Order
    docs = list()
    docs.append(FetchDocument.getHealthDocuments())
    docs.append(FetchDocument.getHistoryDocuments())
    docs.append(FetchDocument.getMathDocuments())
    docs.append(FetchDocument.getPhysicsDocuments())
    docs.append(FetchDocument.getTechDocuments())

    print("docs appended")

    inverted_indexes = list()
    # full_inverted_index = InvertedIndex.InvertedIndex()
    full_docs = list()

    for i in range(5):
        inverted_indexes.append(InvertedIndex.InvertedIndex())

    print("Inverted Indexes Created")

    for i in range(len(docs)):
        for j in range(len(docs[i])):
            for k in range(len(docs[i][j].words)):
                inverted_indexes[i].add_id(docs[i][j].words[k], docs[i][j].doc_id)

    # inverted_indexes[0].print_all()
    # input("***")
    print("Full Inverted Index for All Categories")

    # for i in range(len(inverted_indexes)):
    #     full_inverted_index.merge(inverted_indexes[i].index_array)

    print("All Set up")

    # full_inverted_index.print_all()

    for i in range(len(docs)):
        for j in range(len(docs[i])):
            full_docs.append(docs[i][j])

    centroids = list()
    indexes_scores = list()

    query = 'آزمایش'
    # query = input("Please Enter your Query:\n")

    query_scores = list()
    for i in range(len(docs)):
        centroid, docs_scores = calculate_centroid(inverted_indexes[i], docs[i])
        centroids.append(centroid)
        indexes_scores.append(docs_scores)
        query_scores.append(ScoreCalculator.query_score_calculator(Document.Document(query, 1), docs[i]))

    best_index = find_best_cluster_index(inverted_indexes, centroids, query_scores)

    #    k = input("Please Enter K Value:\n")
    k = 10

    results = ScoreCalculator.score_calculator(inverted_indexes[best_index], docs[best_index], query, k)

    print(results)
