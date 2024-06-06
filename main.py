def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    character_ditionary = {
        k: v
        for k, v in sorted(
            get_num_characters(text).items(), key=lambda item: item[1], reverse=True
        )
    }
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for char in character_ditionary:
        if char.isalpha():
            print(f"The {char} charcter was found {character_ditionary[char]} times")

    print("--- End report ---")


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


main()
