

#  https://leetcode.com/problems/number-of-segments-in-a-string/


class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0

        return len([segment for segment in s.split(" ") if segment != ""])