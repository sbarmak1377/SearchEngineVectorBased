import os


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

def file_reader(path):
    file = open(path, "r", encoding="utf-8")
    lines = []
    line = file.readline()
    while line:
        lines.append(line)
        line = file.readline()
    return lines