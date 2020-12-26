import Document
import InvertedIndex
import RemoveMostCommonWords
import WeightCalculator

def score_calculator(invertedIndex: InvertedIndex, docs, query,k):
    query_doc = Document.Document(query, 1)

