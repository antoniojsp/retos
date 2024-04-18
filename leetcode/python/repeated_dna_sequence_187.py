from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        hash_table = {}
        for i in range(len(s)-9):
            if s[i:i+10] not in hash_table:
                hash_table[s[i:i+10]] = 1

            elif s[i:i + 10] in hash_table:
                hash_table[s[i:i+10]] += 1

        result = [i for i , j in hash_table.items() if j > 1]
        return result





print(Solution().findRepeatedDnaSequences("AAAAAAAAAAA"))