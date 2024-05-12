#https://leetcode.com/problems/largest-local-values-in-a-matrix/description/?envType=daily-question&envId=2024-05-12
from typing import List


class Solution:

    @staticmethod
    def check_greatest(grid, row, col ) ->int:
        maximum = 0
        for i in range(row, row +3):
            for j in range(col, col +3):
                maximum = max(maximum, grid[i][j])
        return maximum


    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        side_len = len(grid ) -2
        result = [[0 for i in range(side_len)] for i in range(side_len)]
        for row in range(0, side_len):
            for col in range(0, side_len):
                result[row][col] = self.check_greatest(grid, row, col)

        return result

