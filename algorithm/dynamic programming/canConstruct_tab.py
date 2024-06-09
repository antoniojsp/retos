


def can_construct(word, wordbank):

    table = [False]*(len(word)+1)
    table[0] = True

    for index, boolean in enumerate(table):
        if boolean:
            for i in wordbank:
                if word[index:index+len(i)] == i:
                    table[index+len(i)] = True
    return table[-1]

print(can_construct("enterapotentpot", ["a","p","ent", "enter", "ot", "o", "t"]))

import unittest

class TestCanConstruct(unittest.TestCase):

    def test_can_construct(self):
        # Test cases
        self.assertTrue(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # Should return True
        self.assertFalse(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # Should return False
        self.assertTrue(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # Should return True
        self.assertFalse(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
            "e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # Should return False

if __name__ == "__main__":
    unittest.main()