def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):

    dict_char = {}

    for t in text:
        lowered = t.lower()
        if lowered not in dict_char:
            dict_char[lowered] = 1
        else:
            dict_char[lowered] += 1

    return dict_char
