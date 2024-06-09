

def count_construct_tab(word, wordbank):

    table = [0]*(len(word)+1)
    table[0] =  1  # empty array has one and just one possible combination

    for index, val in enumerate(table):
        if val > 0:
            for i in wordbank:
                if i == word[index:index+len(i)]:
                    table[index+len(i)] = table[index]+table[index+len(i)]
    return table[-1]

# print(count_construct_tab("purple",["purp","p","ur", "le","purpl"]))
print(count_construct_tab("abcdef",["ab","abc","cd", "def","abcd", "ef", "c"]))
# print(count_construct_tab("enterapotentpot", ["a","p","ent", "enter", "ot", "o", "t"]))
import unittest

class TestCountConstructTab(unittest.TestCase):

    def test_count_construct_tab(self):
        # Test cases
        self.assertEqual(count_construct_tab("purple", ["purp", "p", "ur", "le", "purpl"]), 2)  # Should return 2
        self.assertEqual(count_construct_tab("abcdef", ["ab", "abc", "cd", "def", "abcd"]), 1)  # Should return 1
        self.assertEqual(count_construct_tab("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]),
                         0)  # Should return 0
        self.assertEqual(count_construct_tab("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]),
                         4)  # Should return 4
        self.assertEqual(count_construct_tab("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
            "e", "ee", "eee", "eeee", "eeeee", "eeeeee"]), 0)  # Should return 0


if __name__ == "__main__":
    unittest.main()
