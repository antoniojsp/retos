

def howSum(target, nums):

    if target == 0:
        return []
    if target < 0:
        return None

    for i in nums:
        remainder = target - i
        current = howSum(remainder, nums)
        if current is not None:
            return current + [i]

    return None


def howSum_memo(target, nums, memo = None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == 0:
        return []
    if target < 0:
        return None

    for i in nums:
        remainder = target - i
        current = howSum_memo(remainder, nums, memo)
        if current is not None:
            memo[target] = current + [i]
            return memo[target]

    memo[target] = None
    return memo[target]

print(howSum_memo(300, [2,3]))