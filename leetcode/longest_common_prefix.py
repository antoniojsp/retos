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

# print(longestCommonPrefix(strs))

def isAllEqual(t:tuple)->bool:
    return len(set(t)) <= 1

def longestCommonPrefix1(strs:str)->str:
    result = ""
    for t in zip(*strs):
        if isAllEqual(t):
            result += t[0]
        else:
            break
    return result

print(longestCommonPrefix1(strs))


# class Solution:
#
#     def isAllEqual(self, t: tuple) -> bool:
#         return len(set(t)) <= 1
#
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         result = ""
#         for t in zip(*strs):
#             if self.isAllEqual(t):
#                 result += t[0]
#             else:
#                 break
#         return result
an = [1,2,3,4,5]
a, b , *c = an
print(c)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(i) for i in strs])
        result = []
        i = 0
        while i < min_len:
            temp = set()
            current = ""
            for letter in strs:
                if letter[i] not in temp:
                    temp.add(letter[i])
                current = letter[i]
            if len(temp) > 1:
                break
            i+=1

            result.append(current)
        return "".join(result)