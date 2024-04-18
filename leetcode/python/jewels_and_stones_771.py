
# https://leetcode.com/problems/jewels-and-stones/description/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # set is implemented as a hash table
        jewels_set = set(list(jewels))
        count = 0
        for i in stones:
            if i in jewels_set:
                count+=1

        return count

a = "a, a, a, a, b,b,b,c, c"

print(a.split(","))