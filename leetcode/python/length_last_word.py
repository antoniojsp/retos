class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trim_front_back = s.strip()
        split_list = trim_front_back.split(" ")
        return len(split_list[-1])

    def lengthOfLastWord2(self, s: str) -> int:

        start = False
        count = 0

        for i in range(len(s)-1, -1,-1):
            if start == False and s[i] == " ":
                continue
            else:
                start = True

            if start and s[i] == " ":
                break
            count +=1

        return count








a = Solution()

print(a.lengthOfLastWord2("Hello World"))