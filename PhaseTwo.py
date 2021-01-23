import FetchDocument
import InvertedIndex
import ChampionList
import ScoreCalculator

if __name__ == '__main__':
    docs = FetchDocument.getAllDocuments2()
    inverted_index = InvertedIndex.InvertedIndex()
    for i in range(len(docs)):
        for j in range(len(docs[i].words)):
            inverted_index.add_id(docs[i].words[j], docs[i].doc_id)
#    inverted_index.print_all()
#    k = input("Please Enter K Value:\n")
    k = 10
#    r = input("Please Enter R Value:\n")
    r = 20
#    query = input("Please Enter your Query:\n")
    query = 'تراکتور'
    champion_list = ChampionList.champion_list_creator(inverted_index, docs, r)
#    champion_list.print_all()
    results = ScoreCalculator.score_calculator(champion_list, docs, query, k)
    print(results)
