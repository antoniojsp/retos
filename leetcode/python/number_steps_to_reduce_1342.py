#  https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            coun t+ =1
            if nu m % 2= =0:
                nu m// =2
            else:
                nu m- =1
        return count
