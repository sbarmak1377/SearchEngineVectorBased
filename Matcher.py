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
