import sys

obj = 11
arr = [2, 4]

def canSum(nums:list, target:int):
    if target == 0:
        return True
    if target < 0:
        return False

    for i in nums:
        remainder = target - i
        if canSum(nums, remainder):
            return True

    return False



# def canSum_memo(nums:list, target:int, memo = None):
#
#     if memo is None:
#         memo = {}
#
#     if target in memo:
#         return memo[target]
#     if target == 0:
#         return True
#     if target < 0:
#         return False
#
#     for i in nums:
#         remainder = target - i
#         if canSum_memo(nums, remainder, memo):
#             memo[target] = True
#             return True
#
#     memo[target] =  False
#     return False

import unittest

def canSum_m(nums, target, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for i in nums:
        remainder = target - i
        if canSum_m(nums, remainder, memo):
            memo[target] = True
            return True

    memo[target] = False
    return False

import unittest

canSum_memo = canSum
class TestCanSumMemo(unittest.TestCase):

    def test_can_sum_true_cases(self):
        self.assertTrue(canSum_memo([2, 3], 7))
        self.assertTrue(canSum_memo([5, 3, 4, 7], 7))
        self.assertTrue(canSum_memo([2, 3, 5], 8))

    def test_can_sum_false_cases(self):
        self.assertFalse(canSum_memo([2, 4], 7))
        # self.assertFalse(canSum_memo([7, 14], 300))

    def test_empty_list(self):
        self.assertFalse(canSum_memo([], 7))
        self.assertTrue(canSum_memo([], 0))

    def test_zero_target(self):
        self.assertTrue(canSum_memo([1, 2, 3], 0))

    def test_negative_target(self):
        self.assertFalse(canSum_memo([1, 2, 3], -5))

if __name__ == '__main__':
    unittest.main()