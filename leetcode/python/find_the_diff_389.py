

# https://leetcode.com/problems/find-the-difference/description/
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        # O(s+t)
        temp = s + t
        seen = [0]*26
        for i in temp:
            seen[ord(i)-ord("a")]+=1
        for i, j in enumerate(seen):
            if j%2 != 0:
                return chr(i+ord("a"))

        # using dictionary 0(n) but del can have a 0(n) amortized time complexity
        # seen = {}
        # for i in temp:
        #     if i not in seen:
        #         seen[i] = 0
        #     seen[i] += 1
        #     if seen[i] == 2:
        #         del seen[i]

        # return list(seen.keys())[0]

        # sorting o(n log n)
        # s_list = sorted(s)
        # t_list = sorted(t)
        # i = 0
        # while i < len(s):
        #     if s_list[i] != t_list[i]:
        #         return t_list[i]
        #     i+=1

        # return t_list[-1]
