class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # case if s is empty, then it's a subsequence
        if not s:
            return True
        # case if t is empty and s is not, then it cannot be a subseuence
        if not t and len(s) > 0:
            return False

        current_s_char = 0
        for current_t_char in t:
            #checking for current_s_char in t, if present, look for next one.
            if s[current_s_char] == current_t_char:
                current_s_char += 1
            #if current s char equal to len of s, all s chars in t (in order)
            if current_s_char == len(s):
                return True

        return False





print(Solution().isSubsequence(s = "abc", t = "ahbgdc"))