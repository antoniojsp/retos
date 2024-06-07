
import unittest
def countConstruct(word:str, wordbank:list):
    if word == "":
        return 1

    adding = 0
    for i in wordbank:
        if i == word[:len(i)]:
            remainder = word[len(i):]
            adding+=countConstruct(remainder, wordbank)

    return adding


def countConstruct_memo(word: str, wordbank: list, memo=None):
    if memo is None:
        memo = {}
    if word in memo:
        return memo[word]
    if word == "":
        return 1

    adding = 0
    for i in wordbank:
        if word.startswith(i):  # Ensure we're checking prefixes correctly
            remainder = word[len(i):]
            adding += countConstruct_memo(remainder, wordbank, memo)

    memo[word] = adding
    return adding

class TestCountConstructMemo(unittest.TestCase):

    def test_example_case_1(self):
        self.assertEqual(countConstruct_memo("abcdef", ["ab", "abc", "cd", "def", "abcd"]), 1)

    def test_example_case_2(self):
        self.assertEqual(countConstruct_memo("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]), 0)

    def test_example_case_3(self):
        self.assertEqual(countConstruct_memo("", ["cat", "dog", "mouse"]), 1)

    def test_example_case_4(self):
        self.assertEqual(countConstruct_memo("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]), 4)

    def test_example_case_5(self):
        self.assertEqual(countConstruct_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]), 0)

if __name__ == "__main__":
    unittest.main()


# def countConstruct_memo(target, wordbank, memo=None):
#     """
#     Time complexity: O(N*M^2)
#     Space Complexity: O(M*2)
#     """
#     if memo is None:
#         memo = {}
#     val = memo.get(target)
#     if val is not None:
#         return val
#     if target == "":
#         return 1
#     count = 0
#     for word in wordbank:
#         if target.find(word) == 0:
#             updated_target = target[len(word):]
#             count += countConstruct_memo(updated_target, wordbank, memo)
#
#     memo[target] = count
#     return count


