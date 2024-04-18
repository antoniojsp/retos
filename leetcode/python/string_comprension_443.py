# https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        temp = ""
        current = "a"
        answer = ""





print(Solution().compress(chars = ["a","a","b","b","c","c","c"]))