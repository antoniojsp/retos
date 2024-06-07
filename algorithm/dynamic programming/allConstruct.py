import unittest

def allConstruct(word:str, wordbank:list):

    if word == "":
        return [[]]

    result = []
    for i in wordbank:
        if word.startswith(i):
            remainder = word[len(i):]
            ways =  allConstruct(remainder, wordbank)

            for way in ways:
                result.append([i] + way)

    return result

print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))


class TestAllConstruct(unittest.TestCase):

    def test_empty_word(self):
        self.assertEqual(allConstruct("", ["a", "b", "c"]), [[]])

    def test_no_construction(self):
        self.assertEqual(allConstruct("abc", ["d", "e", "f"]), [])

    def test_single_construction(self):
        self.assertEqual(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]), [['abc', 'def']])

    def test_multiple_constructions(self):
        self.assertEqual(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]),
                         [['purp', 'le'], ['p', 'ur', 'p', 'le']])

    def test_large_input(self):
        self.assertEqual(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]), [
            ['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot'],
            ['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't'],
            ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot'],
            ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']
        ])

    def test_no_wordbank(self):
        self.assertEqual(allConstruct("hello", []), [])


if __name__ == '__main__':
    unittest.main()