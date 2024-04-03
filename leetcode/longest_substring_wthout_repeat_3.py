#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_count = 0
        temp_count = 0
        for i in s:
            if i not in seen:
                temp_count += 1
                seen.add(i)
            else:
                max_count = max(temp_count, max_count)
                temp_count = 1
                seen = set()
                seen.add(i)

        return max_count


print(Solution().lengthOfLongestSubstring("pwwkew"))