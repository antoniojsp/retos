

def best_sum_tab(target, nums):

    table = [None for i in range(target+1)]
    table[0] = []

    for i in range(target+1):
        if table[i] is not None:
            for val in nums:
                if i + val < len(table):
                    combo = table[i] + [val]
                    if table[i+val] is None or len(combo) < len(table[i+val]):
                        table[i + val] = combo

    return table[-1]


import unittest

class TestBestSumTab(unittest.TestCase):
    def test_best_sum_tab(self):
        self.assertEqual(best_sum_tab(7, [5, 3, 4, 7]), [7])
        self.assertEqual(best_sum_tab(8, [2, 3, 5]), [3, 5])
        self.assertEqual(best_sum_tab(8, [1, 4, 5]), [4, 4])
        self.assertEqual(best_sum_tab(100, [1, 2, 5, 25]), [25, 25, 25, 25])
        self.assertIsNone(best_sum_tab(7, [2, 4]))
        self.assertEqual(best_sum_tab(0, [1, 2, 3]), [])

if __name__ == '__main__':
    unittest.main()

# []none none none
# [2,2,2,2][2,3,3][3,5]u