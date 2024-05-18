#  https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75


class Solution:
    def decodeString(self, s: str) -> str:
        S = []
        for i in s:
            if i == "]":
                temp = ""
                while True:
                    char = S.pop()
                    if char == "[":
                        break
                    temp = char + temp
                times = ""
                while S and S[-1].isdigit():
                    times = S.pop() + times
                string = "".join(temp)
                string = string*int(times)
                S.append(string)
            else:
                S.append(i)
        return "".join(S)




print(Solution().decodeString("100[leetcode]"))