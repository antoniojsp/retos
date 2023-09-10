strs = ["flower","flow","flight"]

def longestCommonPrefix(strs):
    min_len = float("inf")
    for i in strs:
        min_len = min(min_len, len(i))

    result = ""
    for i in range(min_len):
        temp = set()
        for j in strs:
            temp.add(j[i])
        if len(temp)>1:
            break
        result += j[i]

    return result

print(longestCommonPrefix(strs))
