
def update(arr, index):
    try:
        arr[index] = True
    except IndexError:
        return

def can_sum_tab(target, nums):

    table = [False]*(target+1)
    table[0] = True

    for i in range(0, target):
        if table[i]:
            for j in nums:
                update(table, i+j)

    return table[-1]


import unittest
class TestCanSumTab(unittest.TestCase):
    def test_can_sum_tab(self):
        self.assertTrue(can_sum_tab(7, [2, 3, 4]))
        self.assertFalse(can_sum_tab(7, [2, 4, 6]))
        self.assertTrue(can_sum_tab(8, [2, 3, 5]))
        self.assertFalse(can_sum_tab(300, [7, 14]))


if __name__ == '__main__':
    unittest.main()
