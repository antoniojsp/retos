class Solution:
    def reverseVowels(self, s: str) -> str:

        left = 0
        right = len(s)-1
        temp = list(s)
        vocals = "aeiou"
        while left <= right:
            if temp[left] not in vocals:
                left += 1
            if temp[right] not in vocals:
                right -= 1
            if temp[left] in vocals and temp[right] in vocals:
                temp[left], temp[right] = temp[right], temp[left]
                left+=1
                right-=1

        return "".join(temp)


print(Solution().reverseVowels(s = "hello"))