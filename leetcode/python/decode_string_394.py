#  https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def decodeString(self, s: str) -> str:
        S = []
        for i in s:
            if i == "]":
                string = ""
                while (char := S.pop()) != "[": #  extract allthbe prev chars
                    string = char + string

                times = ""
                while S and S[-1].isdigit(): #  get the number ot times to repeat
                    times = S.pop() + times

                string = string*int(times)
                S.append(string)
            else:
                S.append(i)
        return "".join(S)






print(Solution().decodeString("100[leetcode]"))