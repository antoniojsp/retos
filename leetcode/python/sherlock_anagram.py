from collections import Counter

def  sherlockAndAnagrams(s):
    result = []
    for i in range(len(s)+1):
        for j in range(i+1,len(s)+1):
            result.append("".join(sorted(s[i:j])))

    is_unique = {}
    number = 0
    for i in result:
        if i in is_unique:
            is_unique[i] +=1
        else:
            is_unique[i] = 1

    for i,j in is_unique.items():
        if len(i) == 1 and j >=2:
            number += j//2
        elif j > 1:
            number  +=j


    print(is_unique)
    return int(number)

a = "ifailuhkqq"
print(sherlockAndAnagrams(a))