# https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75

#https://leetcode.com/problems/find-the-middle-index-in-array/submissions/1211594043/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        from_left = [nums[0]]
        for i in range(1, len(nums)):
            from_left.append(from_left[-1 ] +nums[i])

        from_right = [nums[-1]]
        for i in range(len(nums ) -2, -1 ,-1):
            from_right.append(from_right[-1 ] +nums[i])

        from_right.reverse()
        result = -1
        for index, (i ,j) in enumerate(zip(from_left, from_right)):
            if i == j:
                result = index
                break

        return result

