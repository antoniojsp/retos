from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

def can_construct_suffix(word:str, wordbank:list):
    if word == "":
        return True

    for i in wordbank:
        if i  == word[:len(i)]:
            remainder = word[len(i):]
            if can_construct_suffix(remainder, wordbank):
                return True
    return False

def can_construct_suffix_memo(word:str, wordbank:list, memo = None):

    if memo is None:
        memo = {}

    if word in memo:
        return memo[word]

    if word == "":
        return True

    for i in wordbank:
        if i  == word[:len(i)]:
            remainder = word[len(i):]
            if can_construct_suffix_memo(remainder, wordbank, memo):
                memo[word] =  True
                return True
    memo[word] = False
    return False

@timeit
def entry(word, wordbank):
    return can_construct_suffix_memo(word, wordbank)


print(entry("eeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", 'eeeeeee']))



import unittest

class TestCanConstructSuffix(unittest.TestCase):

    def test_empty_word(self):
        self.assertTrue(can_construct_suffix_memo("", ["a", "b", "c"]))

    def test_word_can_be_constructed(self):
        self.assertTrue(can_construct_suffix_memo("abcd", ["a", "b", "cd", "ab"]))
        self.assertTrue(can_construct_suffix_memo("apple", ["a", "p", "le", "ppl", "app"]))
        self.assertTrue(can_construct_suffix_memo("catsanddog", ["cats", "dog", "and", "cat", "sand"]))
        self.assertTrue(can_construct_suffix_memo("hello", ["he", "ll", "o", "l"]))
        self.assertTrue(can_construct_suffix_memo("purple", ["pur", "p", "ur", "le"]))
        self.assertTrue(can_construct_suffix_memo("world", ["wo", "r", "ld"]))
        self.assertTrue(can_construct_suffix_memo("antidisestablishmentarianism", ["anti", "dis", "establishment", "arian", "ism"]))
    def test_word_cannot_be_constructed(self):
        self.assertFalse(can_construct_suffix_memo("abcd", ["a", "b", "c"]))
        self.assertFalse(can_construct_suffix_memo("hello", ["he", "lo", "ell"]))
        self.assertFalse(can_construct_suffix_memo("world", ["w", "or", "l", "worl"]))
    def test_empty_wordbank(self):
        self.assertFalse(can_construct_suffix_memo("abc", []))

    def test_wordbank_with_longer_words(self):
        self.assertFalse(can_construct_suffix_memo("short", ["longer", "words"]))


if __name__ == '__main__':
    unittest.main()

    # print(can_construct_suffix_memo("anti dis establishment arian ism", ["anti", "dis", "establishment", "arian", "ism"]))




# def can_construct(word: str, current: str, wordbank: list, memo=None):
#     if memo is None:
#         memo = {}
#
#     if current in memo:
#         return memo[current]
#     if current == word:
#         return True
#
#     if len(word) < len(current):
#         return False
#     wordbank = sorted(wordbank, key=len, reverse=True)
#     for i in wordbank:
#         if can_construct(word, current + i, wordbank, memo):
#             memo[current] = True
#             return True
#
#     memo[current] = False
#     return False


