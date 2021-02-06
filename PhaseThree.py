import FetchDocument
import InvertedIndex
import ScoreCalculator
import Document
import CosinusCalculator


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
        helper.sort()
        centroid_helpers.append(helper)
    for i in range(len(query_scores)):
        helper = CosinusCalculator.CosinusHelper()
        for j in range(len(query_scores[i])):
            helper.words.append(query_scores[i][j][0])
            helper.weights.append(query_scores[i][j][1])
        helper.sort()
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
