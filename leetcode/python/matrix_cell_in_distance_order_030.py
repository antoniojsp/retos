#https://leetcode.com/problems/matrix-cells-in-distance-order/description/
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        distances = []
        for i in range(rows):
            for j in range(cols):
                distance = abs(i - rCenter) + abs(j - cCenter)
                distances.append([distance, (i, j)])
        x = lambda x: x[0]
        distances.sort(key=x)
        result = map(lambda x: x[1], distances)

        return result
