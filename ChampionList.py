import InvertedIndex
import WeightCalculator
import Document


def champion_list_creator(invertedIndex: InvertedIndex, docs, r):
    result = InvertedIndex.InvertedIndex()
    for i in range(len(invertedIndex.index_array)):
        word = invertedIndex.index_array[i].word
        arr = invertedIndex.index_array[i].doc_ids
        temp_res = []
        for j in range(len(arr)):
            id_location = Document.documents_binary_search(docs, 0, len(docs) - 1, arr[j])
            weight = WeightCalculator.weight_calculator_doc(word, docs, docs[id_location])
            temp_res.append([arr[j], weight])
        res = sorter(temp_res, r)
        index = InvertedIndex.Index(word)
        index.set_docs_id(res)
        result.index_array.append(index)
    return result


def sorter(temp_res, r):
    res = []
    for i in range(len(temp_res)):
        for j in range(len(temp_res)):
            if temp_res[j][1] > temp_res[i][1]:
                tmp = temp_res[j]
                temp_res[j] = temp_res[i]
                temp_res[i] = tmp
    if len(temp_res) > r:
        for i in range(r):
            res.append(temp_res[i][0])
    else:
        for i in range(len(temp_res)):
            res.append(temp_res[i][0])
    return sorted(res)
