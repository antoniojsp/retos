

#https://leetcode.com/problems/island-perimeter/description/
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        Q = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    Q.append((row, col))
        count = 0

        for i, j in Q:
            if ( i -1 >= 0 and grid[ i -1][j] == 0) or (i == 0):
                coun t+ =1
            if ( i +1 < len(grid) and grid[ i +1][j] == 0) or (i == len(grid ) -1):
                coun t+ =1
            if ( j -1 >= 0 and grid[i][ j -1] == 0) or (j == 0):
                coun t+ =1
            if ( j +1 < len(grid[0]) and grid[i][ j +1] == 0) or (j == len(grid[0] ) -1):
                coun t+ =1

        return count


