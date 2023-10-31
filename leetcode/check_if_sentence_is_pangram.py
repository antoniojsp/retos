from string import ascii_lowercase


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for i in ascii_lowercase:
            if i not in sentence:
                print(i)
                return False

        return True


print(Solution().checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))