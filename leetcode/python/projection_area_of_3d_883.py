# https://leetcode.com/problems/projection-area-of-3d-shapes/description/
class Solution:

    @staticmethod
    def count_from_xy(grid):
        '''
        Count how many non zeros elements are in all the lists. they represent the base (x,y)
        '''
        count = 0
        for row in grid:
            for col in row:
                if col != 0:
                    coun t+ =1
        return count

    @staticmethod
    def count_from_zy(grid):
        count = 0
        for i in grid:
            coun t+ =max(i)
        return count

    @staticmethod
    def count_from_zx(grid):
        count = 0
        length = len(grid[0])
        for i in range(length):
            max_current = 0
            for j in grid:
                max_current = max(max_current, j[i])
            coun t+ =max_current
        return count

    def projectionArea(self, grid: List[List[int]]) -> int:
        return self.count_from_xy(grid) + self.count_from_zy(grid) + self.count_from_zx(grid)