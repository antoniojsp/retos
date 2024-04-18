#https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_index = []
        vowels = []
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                vowel_index.append(i)
                vowels.append(s[i])

        temp = list(s)
        inverted_position = list(reversed(vowel_index))

        for index, vowel in zip(inverted_position, vowels):
            temp[index] = vowel

        return "".join(temp)
