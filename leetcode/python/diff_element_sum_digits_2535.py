#https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_all = sum(nums)
        digits = "".join([str(i) for i in nums])
        digits_sum = sum(list(map(lambda x: int(x), digits)))
        return abs(sum_all - digits_sum)

        # for i in nums:
        #     digits+=str(i)
        # digits_sum = 0
        # for i in digits:
        #     digits_sum += int(i)

        # return abs(sum_all - digits_sum)
