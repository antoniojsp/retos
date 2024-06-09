import unittest


def all_construct(target:str, wordbank:list) -> list:
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for index, val in enumerate(target):
        for word in wordbank:
            if word == target[index:index + len(word)]:
                temp = []
                for j in table[index]:
                    temp.append(j + [word])
                for k in temp:
                    table[index + len(word)].append(k)

    return table[-1]

print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct("aaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa", "z"]))

target = "abcdef"
wordbank = ["ab", "abc", "cd", "def", "abcd", "ef", "c"]
print(all_construct(target, wordbank))