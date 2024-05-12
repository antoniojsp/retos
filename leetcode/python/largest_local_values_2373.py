class Solution:

    @staticmethod
    def check_greatest_in_grid(grid: list, row: int, col: int) -> int:
        '''
        Check row by row from the 3x3 area of the grid for the greatest value.
        '''
        maximum = 0
        for i in grid[row:row + 3]:
            max_of_row = max(i[col:col + 3])
            maximum = max(maximum, max_of_row)
        return maximum

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        side_len = len(grid) - 2
        result = [[0 for i in range(side_len)] for i in range(side_len)]
        for row in range(0, side_len):
            for col in range(0, side_len):
                result[row][col] = self.check_greatest_in_grid(grid, row, col)

        return result

