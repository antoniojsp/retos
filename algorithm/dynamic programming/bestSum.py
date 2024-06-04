

def best_sum(target:int, nums:list):

    if target == 0:
        return []

    if target < 0:
        return None

    shortest = None

    for i in nums:
        remainder = target - i
        best = best_sum(remainder, nums)
        if best is not None:
            combination  = best + [i]
            if shortest is None or len(combination) < len(shortest):
                shortest = combination

    return shortest

print(best_sum(8, [1,2,3]))
