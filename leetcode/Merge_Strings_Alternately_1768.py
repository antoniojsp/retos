class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Not checking if the strings are empty since the problem's constraints
        specify that they are at least size 1.
        """
        i = 0
        j = 0
        result = ''
        while i < len(word1) and j < len(word2):
            result += f"{word1[i]}{word2[j]}"
            i+=1
            j+=1


        if i < len(word1):
            result += word1[i:]
        elif j < len(word2):
            result += word2[j:]

        return result


print(Solution().mergeAlternately(word1 = "ab", word2 = "pqrs"))