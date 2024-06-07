

def how_sum_tab(target, nums):

    table = [None for i in range(target+1)]
    table[0] = []

    for i in range(len(table)):
        if table[i] is not None:
            for val in nums:
                try:
                    table[i+val] = table[i] + [val]
                except IndexError:
                    continue
    return table[-1]

# print(how_sum_tab(0, [1,2,4]))
import unittest
class TestHowSumTab(unittest.TestCase):
    def test_how_sum_tab(self):
        self.assertIn(how_sum_tab(7, [2, 3]), [[2, 2, 3], [3, 2, 2], [2, 3, 2]])
        self.assertIn(how_sum_tab(7, [5, 3, 4, 7]), [[7], [3, 4], [4, 3]])
        self.assertIsNone(how_sum_tab(7, [2, 4]))
        self.assertIn(how_sum_tab(8, [2, 3, 5]), [[3, 5], [5, 3], [2, 2, 2, 2]])
        self.assertIsNone(how_sum_tab(300, [7, 14]))
        self.assertEqual(how_sum_tab(0, [1, 2, 3]), [])

if __name__ == '__main__':
    unittest.main()

