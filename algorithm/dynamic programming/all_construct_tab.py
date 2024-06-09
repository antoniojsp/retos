

def all_construct(word:str, wordbank:list) -> list:

    table = [[]]*(len(word)+1)
    table[0] = [[]]

    for index, val in enumerate(table):
        if len(val) > 0:
            for i in wordbank:
                if i == word[index:index+len(i)]:
                    for k, j  in enumerate(table[index]):
                        table[index+len(i)].append(j)


    print(table)

print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))


