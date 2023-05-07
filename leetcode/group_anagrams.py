# strs = ["",""]
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    val =  strs.copy()

    if len(strs) == 1:
        return [strs]


    for i in range(len(strs)):
        if strs[i] == '':
            strs[i] = ''
        else:
            strs[i] = sorted(strs[i])

    result = []
    visited = set()
    for i in range(len(strs)):

        if strs[i] == '':
            pass
        elif  not strs[i]:
            continue

        temp = [val[i]]
        for j in range(i+1, len(strs)):

            if j not in visited and strs[i] == strs[j]:
                temp.append(val[j])
                strs[j] = []
                visited.add(j)

        result.append(temp)

    return result

# print(groupAnagrams(strs))
def groupAnagrams1(strs: list[str]) -> list[list[str]]:
    data = {}
    sorted_strings = ["".join(sorted(i)) for i in strs]
    for i, j in enumerate(sorted_strings):
        if j not in data:
            data[j] = []
        data[j].append(strs[i])
    result = [i for i in data.values()]

    return result

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams1(strs))