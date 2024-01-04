class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.image = copy.deepcopy(rectangle)

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        i = row1
        while i <= row2:
            j = col1
            while j <= col2:
                self.image[i][j] = newValue
                j += 1
            i += 1

    def getValue(self, row: int, col: int) -> int:
        return self.image[row][col]

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)