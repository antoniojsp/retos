from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = []
        for i in range(1,numRows+1):
            temp = [0]*i
            result.append(temp)

        return result


a = Solution().generate(5)
print(a)