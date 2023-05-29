class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start < end:
            middle = start + (end - start) // 2

            if isBadVersion(middle):
                end = middle
            else:
                start = middle + 1

        return start
