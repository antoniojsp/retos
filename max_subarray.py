def is_all_negative(arr: list) -> bool:
    for i in arr:
        if i >= 0:
            return False
    return True


def is_all_positive(arr: list) -> bool:
    for i in arr:
        if i < 0:
            return False
    return True


def subarray(arr: list) -> int:
    current = 0
    result = 0
    for i in arr:
        current = max(0, current + i)
        result = max(current, result)
    return result


def subsequence(arr: list) -> int:
    pos = lambda x: True if x >= 1 else False
    return sum(filter(pos, arr))


def maxSubarray(arr):
    # Write your code here
    if is_all_negative(arr):
        result = max(arr)
        return [result, result]
    if is_all_positive(arr):
        result = sum(arr)
        return [result, result]

    return [subarray(arr), subsequence(arr)]