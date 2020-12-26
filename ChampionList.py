import InvertedIndex
import WeightCalculator
import Document


def champion_list_creator(invertedIndex: InvertedIndex, docs, k):
    result = InvertedIndex()
    for i in range(len(invertedIndex.index_array)):
        word = invertedIndex.index_array[i].word
        arr = invertedIndex.index_array[i].doc_ids
        temp_res = []
        for j in range(len(arr)):
            id_location = Document.documents_binary_search(docs, 0, len(docs) - 1, arr[j])
            tf = docs[id_location].words_dictionary.get(word)
            idf = WeightCalculator.idf(word, docs)
            weight = WeightCalculator.weight_calculator_doc(word, docs, docs[id_location])
            temp_res.append([arr[j], weight])
        res = soter(temp_res, k)
        index = InvertedIndex.Index(word)
        index.set_docs_id(res)
        result.index_array.append(index)
    return result



def soter(temp_res, k):
    res = []
    for i in range(len(temp_res)):
        for j in range(len(temp_res)):
            if temp_res[j][1] > temp_res[i][1]:
                tmp = temp_res[j]
                temp_res[j] = temp_res[i]
                temp_res[i] = tmp
    for i in range(k):
        res.append(temp_res[k][0])
    return sorted(res)
