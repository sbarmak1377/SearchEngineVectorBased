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
        for i in range(len(query_res)):
            temp.words.append(query_res[0])
            temp.weights.append(query_res[1])
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


def find_index_cosinus_helper(arr, doc_id):
    for i in range(len(arr)):
        if arr[i].id == doc_id:
            return i
    return -1
