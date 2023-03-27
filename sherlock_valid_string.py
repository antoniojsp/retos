from collections import Counter


def isValid(s):
    count = list(Counter(s).values())
    #case 1 frequency all char are equal
    temp = set(count)
    print(count)
    print(temp)
    if len(temp) == 1:
        return "YES"
    #case 2 more than 2 frequancies
    if len(temp) > 2:
        return "NO"
    list_set = list(temp)

    if count.count(1) > 1 :
        return "NO"

    if abs(list_set[0]-list_set[1]) > 1:
        return "NO"

    return "YES"



test = ["aabbcd"]

for i in test:
    print(isValid(i))



