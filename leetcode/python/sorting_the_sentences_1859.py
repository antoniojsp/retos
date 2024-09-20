
class Solution:
    def sortSentence(self, s: str) -> str:

        sep = s.split()
        result = ["" ] *len(sep)
        for i in sep:
            index = i[-1]
            result[int(index ) -1] = i[:len(i ) -1]

        return " ".join(result)
