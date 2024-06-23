from typing import List
from math import prod
test:List[int] = [23,1,4,56,0,11,14,90,57,120,120]
test2:List[int] = [-5,-2,-1,0,0,1,1,5]
test3:list[int] = [-5,-2]


def top_three(arr:list):
    if len(arr) < 3:
        raise ValueError("Not enough elements.")

    first = float("-inf")
    second = float("-inf")
    third = float("-inf")

    for val in arr:
        if first < val:
            third = second
            second = first
            first = val
        elif second < val:
            third = second
            second = val
        elif third < val:
            third = val
    return first, second, third


def bottom_three(arr: list):
    if len(arr) < 3:
        raise ValueError("Not enough elements.")

    first = float("inf")
    second = float("inf")
    third = float("inf")

    for val in arr:
        if first > val:
            third = second
            second = first
            first = val
        elif second > val:
            third = second
            second = val
        elif third > val:
            third = val
    return first, second, third


def highest_product_of_three(arr:list):
    try:
        hi1, hi2, hi3 = top_three(arr)
        lo1, lo2, lo3 = bottom_three(arr)
    except ValueError as e:
        print(e)


    return max(prod([hi1,hi2,hi3]), prod([lo1,lo2,hi1]))


print(highest_product_of_three(test))


