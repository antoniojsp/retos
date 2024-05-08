

#  https://leetcode.com/problems/relative-ranks/
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        values_positions = [(i, j) for i, j in enumerate(score)]
        values_positions.sort(reverse=True, key=lambda x: x[1]) #  sorted by value

        for index, (i, j) in enumerate(values_positions):
            match index:
                case 0:
                    score[i] = "Gold Medal"
                case 1:
                    score[i] = "Silver Medal"
                case 2:
                    score[i] = "Bronze Medal"
                case _:
                    score[i] = str(index+1)

        return score