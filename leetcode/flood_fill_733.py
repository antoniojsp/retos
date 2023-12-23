from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        value = image[sr][sc]
        row = len(image)
        column = len(image[0])

        def helper(r, c, colour, storage = None):

            if not storage:
                storage = set()
            if f"{r},{c}" in storage:
                return
            if r < 0 or r >= row or c < 0 or c >= column:
                return
            if image[r][c] != value:
                return

            image[r][c] = colour
            storage.add(f"{r},{c}")

            helper(r-1, c, colour, storage)
            helper(r+1, c, colour, storage)
            helper(r, c-1, colour, storage)
            helper(r, c+1, colour, storage)

        helper(sr, sc, color)
        return image
