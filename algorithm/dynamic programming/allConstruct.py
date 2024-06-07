import unittest

def allConstruct(word:str, wordbank:list):

    if word == "":
        return [[]]

    result = []
    for prefix in wordbank:
        if word.startswith(prefix):
            suffix = word[len(prefix):]
            ways =  allConstruct(suffix, wordbank)
            ways = map(lambda x:[prefix]+x, ways)
            for i in ways:
                result.append(i)
    return result

# print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))

def allConstruct_memo(word:str, wordbank:list, memo= None):

    if memo is None:
        memo = {}

    if word in memo:
        return memo[word]

    if word == "":
        return [[]]

    result = []
    for prefix in wordbank:
        if word.startswith(prefix):
            suffix = word[len(prefix):]
            ways =  allConstruct_memo(suffix, wordbank, memo)
            ways = map(lambda x:[prefix]+x, ways)
            for i in ways:
                result.append(i)

    memo[word] = result
    return result


class TestAllConstruct(unittest.TestCase):
    def test_allConstruct_memo(self):
        self.assertEqual(allConstruct_memo("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]),
                         [['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']])

        self.assertEqual(allConstruct_memo("purple", ["purp", "p", "ur", "le", "purpl"]),
                         [['purp', 'le'], ['p', 'ur', 'p', 'le']])

        self.assertEqual(allConstruct_memo("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]),
                         [])

        self.assertEqual(allConstruct_memo("", ["cat", "dog", "mouse"]),
                         [[]])

        self.assertEqual(allConstruct_memo("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]),
                         [['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot'],
                          ['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't'],
                          ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot'],
                          ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']])

        self.assertEqual(allConstruct_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                                           ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]),
                         [])


if __name__ == "__main__":
    unittest.main()