import unittest

def allConstruct(word:str, wordbank:list):

    if word == "":
        return [[]]

    result = []
    for i in wordbank:
        if word.startswith(i):
            remainder = word[len(i):]
            print(remainder)
            ways =  allConstruct(remainder, wordbank)

            for way in ways:
                result.append([i] + way)

    return result
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
class TestAllConstruct(unittest.TestCase):

    def test_empty_word(self):
        self.assertEqual(allConstruct("", ["cat", "dog", "mouse"]), [])

    def test_single_word_match(self):
        self.assertEqual(allConstruct("cat", ["cat", "dog", "mouse"]), ["cat"])

    def test_multiple_word_match(self):
        self.assertEqual(allConstruct("catsanddog", ["cat", "cats", "and", "sand", "dog"]), ["cats", "and", "dog"])

    def test_no_match(self):
        self.assertEqual(allConstruct("catdog", ["mouse", "elephant", "tiger"]), None)

    def test_partial_match(self):
        self.assertEqual(allConstruct("catdog", ["cat", "elephant", "tiger"]), None)

    def test_full_match(self):
        self.assertEqual(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]), ["abc", "def"])

# if __name__ == '__main__':
#     unittest.main()
