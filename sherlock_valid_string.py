from collections import Counter


from collections import Counter


def isValid(s):
    count = list(Counter(s).values())
    frequencies = set(count)

    if len(frequencies) == 1:
        return "YES"
    if len(frequencies) > 2:
        return "NO"
    one_time_frequency = count.count(1)
    if one_time_frequency == 1:
        return "YES"
    if one_time_frequency > 1 :
        return "NO"
    list_set = list(frequencies)
    if abs(list_set[0]-list_set[1]) == 1:
        return "YES"

    return "NO"



test = ["aabbcd"]

for i in test:
    print(isValid(i))



