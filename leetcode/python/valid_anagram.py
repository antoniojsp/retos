from collections import Counter

class Solution:

    # def counter(self, word:str)->dict:
    #     results = {}

    #     for i in word:
    #         if i not in results:
    #             results[i] = 0
    #         results[i]+= 1
    # gffgddfgdf
    #     return results

    def isAnagram(self, s: str, t: str) -> bool:
        # return self.counter(s) == self.counter(t)
        # return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False

        return "".join(sorted(s)) == "".join(sorted(t))
