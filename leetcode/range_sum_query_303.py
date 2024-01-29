from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        acc = 0
        self.storage = [0]
        for i in nums:
            acc += i
            self.storage.append(acc)

    def sumRange(self, left: int, right: int) -> int:
        return self.storage[right + 1] - self.storage[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)