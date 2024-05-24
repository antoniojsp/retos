from collections import Counter

def count_words(file_location:str)->int:

    with open(file_location, "r") as file:
        answer = file.read().split()

    return len(answer)

def ranking_words(file_location:str)->dict:
    with open(file_location, "r") as file:

        answer = file.read().split()

    result = list(Counter(answer).items())
    result.sort(reverse=True, key=lambda x:x[1])
    return result

if __name__ == "__main__":
    print(ranking_words("text.txt"))
    print(count_words("text.txt"))

