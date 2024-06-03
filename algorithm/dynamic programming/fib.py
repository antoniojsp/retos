import fibonacci
from fibonacci import fibo

def fib(num:int, memo = {}):

    if num in memo:
        return memo[num]

    if num == 0:
        return 0
    if num == 1:
        return 1

    memo[num] = fib(num-2)+fib(num-1)

    return memo[num]

import unittest

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        for i in range(100):
            self.assertEqual(fibonacci.fibo(i), fib(i), "Something went wrong.")

if __name__ == '__main__':
    unittest.main()