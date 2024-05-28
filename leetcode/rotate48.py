#  https://leetcode.com/problems/rotate-image/description/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = []
        for i in range(len(matrix)):
            t = []
            for j in range(len(matrix[0])):
                t.append(matrix[j][i])
            temp.append(t[::-1])

        for i in range(len(matrix)):
            matrix[i] = temp[i]

