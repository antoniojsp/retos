import sys
sys.path.append('../')

from algorithm.sieve_ratosthenes import sieve

with open("primes2.txt") as primes:

    temp = primes.read().split()
    data = list(map(lambda x: int(x), temp))

import unittest

class TestSieve(unittest.TestCase):

    def testing_sieve(self):

        for i , j in zip(sieve(8000), data):
            self.assertEqual(i, j)


if __name__ == '__main__':
    unittest.main()
