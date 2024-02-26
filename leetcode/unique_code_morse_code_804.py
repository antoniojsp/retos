from string import ascii_lowercase
from typing import List


class Solution:
    #creates dict with correspondant morse translation of each letter
    def __init__(self):
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                 "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        self.dict_morse = {}
        for i, j in zip(ascii_lowercase, morse):
            self.dict_morse[i] = j

    # translate a word to morse
    def translate(self, morse_code:str)->str:
        result = ""
        for i in morse_code:
            result += self.dict_morse[i]
        return result

    # translate all words in list and add to set. all items in set are unique.
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        trans_set = set()
        for i in words:
            trans_set.add(self.translate(i))
        return len(trans_set)


print(Solution().uniqueMorseRepresentations(["gin","zen","gig","msg"]))