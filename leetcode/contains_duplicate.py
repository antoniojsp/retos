#https://leetcode.com/problems/contains-duplicate/description/
def containsDuplicate(nums: list[int]) -> bool:
    # return len(nums) != len(set(nums))
    seen = {}
    for i in nums:
        if i in seen:
            return False
        seen[i] = 0

    return True


print(containsDuplicate([1,2,3,1]))