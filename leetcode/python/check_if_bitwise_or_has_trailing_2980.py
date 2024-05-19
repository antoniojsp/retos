#  https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/description/
class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        '''
        Only even number has trailing zeros, which means only xor operations with
        even number can result a number with trailing zeros in its binary form
        '''
        times = 0
        i = 0
        while i < len(nums):
            if nums[i ] % 2= =0:
                time s+ =1
            if times > =2:
                return True i+=1

        r eturn False


        # o(n) space
        # result = [i for i in nums if i%2 == 0]
        # return len(result) >= 2
