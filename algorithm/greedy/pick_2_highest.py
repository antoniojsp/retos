from typing import List

test:List[int] = [23,1,4,56,0,11,14,90,57,120]

def two_greatest(arr:list) -> tuple:
    first:float = float("-inf")
    second:float = float("-inf")
    for i in arr:
        if first < i:
            second = first
            first = i
        elif second < i:
            second  = i

    return first, second

print(two_greatest(test))