import math
import MaxHeap
from InvertedIndex import InvertedIndex


class CosinusHelper:
    id = -1
    words = []
    weights = []

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def sort(self):
        for i in range(len(self.words)):
            for j in range(len(self.words)):
                if self.words[j] < self.words[i]:
                    temp = self.words[j]
                    self.words[j] = self.words[i]
                    self.words[i] = temp
                    temp = self.weights[j]
                    self.weights[j] = self.weights[i]
                    self.weights[i] = temp


class CosinusArray:
    helper_array = []

    def __init__(self, query_res, docs_res):
        temp = CosinusHelper()
        # print(query_res)
        # print(docs_res)
        for i in range(len(query_res)):
            temp.words.append(query_res[i][0])
            temp.weights.append(query_res[i][1])
        temp.sort()
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