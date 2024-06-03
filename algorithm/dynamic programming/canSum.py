

obj = 11
arr = [2, 4]

def canSum(nums:list, target:int):
    if target == 0:
        return True
    if target < 0:
        return False

    for i in nums:
        remainder = target - i
        if canSum(nums, remainder):
            return True

    return False



def canSum_memo(nums:list, target:int, memo = None):

    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for i in nums:
        remainder = target - i
        memo[remainder] = canSum_memo(nums, remainder, memo)
        if memo[remainder]:
            return True

    return False

print(canSum_memo([1, 7, 14], 300))