from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        name_height_tuples = [(i,j) for i,j in zip(names, heights)]
        name_height_tuples.sort(key=lambda x: x[1], reverse=True)
        return [i[0]for i in name_height_tuples]


print(Solution().sortPeople( ["Mary","John","Emma"], [180,165,170]))