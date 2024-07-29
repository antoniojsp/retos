

text = "My study adds to My study"


def count_unique_words(word:str) -> int:
    word_list = word.split(" ")
    unique = set(word_list)
    return len(unique)

print(count_unique_words(text))
