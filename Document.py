from File import *
import RemoveMostCommonWords


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
    string = string.replace("{", "")
    string = string.replace("}", "")
    string = string.replace("»", "")
    string = string.replace("؛", "")
    string = string.replace("/", "")
    string = string.replace("؟", "")
    string = string.replace("،", "")
    string = string.replace(":", "")
    return string


class Document:
    word_count = 0
    doc_id = -1
    words_dictionary = dict()
    words = list()

    def __init__(self, path, type: int):
        self.words = list()
        if type == 0:
            self.doc_id = int(path.split("/")[-1][:-4])
            lines = file_reader(path)
            for x in lines:
                new_words = tokenizer(x)
                self.word_count += len(new_words)
                for y in new_words:
                    self.words.append(y)
                    if y in self.words_dictionary:
                        self.words_dictionary[y] += 1
                    else:
                        self.words_dictionary[y] = 1
        elif type == 1:
            self.doc_id = -1
            new_words = tokenizer(path)
            new_words = RemoveMostCommonWords.remove_common_words_from_query(new_words)
            self.word_count += len(new_words)
            for y in new_words:
                self.words.append(y)
                if y in self.words_dictionary:
                    self.words_dictionary[y] += 1
                else:
                    self.words_dictionary[y] = 1


    def __eq__(self, other):
        if self.doc_id == other.doc_id and self.word_count == other.word_count:
            return True
        else:
            return False


    def __lt__(self, other):
        return self.doc_id < other.doc_id


def documents_binary_search(docs, start, end, id):
    if end >= start:

        mid = start + (end - start) / 2

        if docs[mid].doc_id == id:
            return mid

        elif docs[mid].doc_id > id:
            return documents_binary_search(docs, start, mid - 1, id)

        else:
            return docs(docs, mid + 1, end, id)

    else:
        return -1


if __name__ == '__main__':
    path = "Docs/10.txt"
    a = Document(path, 0)
    print(a.doc_id)
    print(a.word_count)
    print(a.words)
    print(a.words_dictionary)
