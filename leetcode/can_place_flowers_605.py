from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # edge case, list has just one element.
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return n <= 1
            elif flowerbed[0] == 1:
                return n == 0

        i = 0
        count = 0
        end = len(flowerbed)
        while i < end:
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    count += 1
            elif i < end - 1:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    count += 1
            elif i == end - 1:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    count += 1
            i += 1

        return count >= n