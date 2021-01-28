class Index:
    word = ""
    doc_ids = list()

    def __init__(self, word):
        self.word = word
        self.doc_ids = list()

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

    def set_docs_id(self, docs):
        self.doc_ids = sorted(docs)

    def __eq__(self, other):
        return self.word == other.word and len(self.doc_ids) == len(other.doc_ids)

    def __lt__(self, other):
        return self.word < other.word


class InvertedIndex:

    def __init__(self):
        self.index_array = list()

    def remove_word(self, word):
        for i in range(len(self.index_array)):
            if self.index_array[i].word == word:
                self.index_array.remove(i)
                return

    def find_word(self, word):
        for i in range(len(self.index_array)):
            if self.index_array[i].word == word:
                return i
        return -1

    def add_word(self, word):
        if self.find_word(word) < 0:
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
                self.index_array[ind].add_id(doc_id)
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

    def merge(self, index_array):
        for x in index_array:
            print(x)
            print(x.word)
            loc = self.find_word(x.word)
            if loc == -1:
                self.add_word(x)
                for id in x.doc_ids:
                    self.add_id(x, id)
            else:
                merged = self.sub_merge(self.index_array[loc].doc_ids, x.doc_ids)
                self.index_array[loc].doc_ids = merged


    def sub_merge(self, word_docs, doc_ids):
        p1 = 0
        p2 = 0
        res = list()
        while p1 < len(word_docs) and p2 < len(doc_ids):
            if word_docs[p1] == doc_ids[p2]:
                res.append(word_docs[p1])
                p1 += 1
                p2 += 1
            elif word_docs[p1] > doc_ids[p2]:
                res.append(doc_ids[p2])
                p2 += 1
            else:
                res.append(word_docs[p1])
                p1 +=1
        res = res + word_docs[p1:] + doc_ids[p2:]
        return res


    def print_all(self):
        for i in range(len(self.index_array)):
            print(self.index_array[i].word)
            print(self.index_array[i].doc_ids)