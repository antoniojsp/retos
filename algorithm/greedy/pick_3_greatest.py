from typing import List

test:List[int] = [23,1,4,56,0,11,14,90,57,120]

def three_greatest(arr:list) -> tuple:
    first:float = float("-inf")
    second:float = float("-inf")
    third:float = float("-inf")
    for i in arr:
        if first < i:
            third = second
            second = first
            first = i
        elif second < i:
            third = second
            second  = i
        elif third < i:
            third = i

    return first, second, third

print(three_greatest(test))