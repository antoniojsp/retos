
def sansaXor(arr:list):
    """
    len(arr) % 2 != 0:
    We are told that the list [3,4,5] would produce the substrings 3 - 4 - 5 - 3,4 - 4,5 - 3,4,5 substrings,
    and that we would need to xor all this values 3 xor 4 xor 5 xor 3 xor 4 xor 4 xor 5 xor 3 xor 4 xor 5.
    Now, we know if we xor two equal values, we would get 0, So, if we get even number of any value,
    we could just cancel them since it produce zero. We return to the [3,4,5] example and get that final operation would be

    3 xor 3 xor 3 xor 4 xor 4 xor 4 xor 4 xor 5 xor 5 xor 5,
    from here, we could easily cancel "4 xor 4 xor 4 xor 4" since it produce zero
    so we are left with 3 xor 3 xor 3 xor 5 xor 5 xor 5, we again cancel 2 equal values, since 3 xor 3 produce 0 and same with 5 xor 5
    so we are left with 3 xor 5, which produce 6

    We observe that the elements from the original array that are located in even "position" (0 first, 2 third, 4 fifth, etc)
    will produce un even number of values once all the substrings are produce. How much is 3 xor 3 xor 3?? 3, we cancel 3 xor 3 and
    get only 3. Same for 5 xor 5 xot 5 xor 5 xor 5 xor 5, we would cancel the first 4 xor and remain with 5.
    So, since the odd positions from the original array will produce odd number of values at the end, we can just focus
    in perform the operations of xor with the elements at odd position (0,2,4, etc).

    len(arr) % 2==0:
    if the length of the array is even, then we simple return 0 as a result of the xor operations in that array.
    """
    if len(arr)%2 == 0:
        return 0
    result = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            result ^= arr[i]

    return result

print(sansaXor([1, 2, 3, 4, 6]))


# !/bin/python3
# https://www.hackerrank.com/challenges/three-month-preparation-kit-sansa-and-xor/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-five
import math
import os
import random
import re
import sys


#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
#
#
# def sansaXor(arr):
#     # Write your code here
#     """
#     if len(arr) is even, then getting all the posible combinations of subarrays would contain numbers in pairs. if it's odd, then the solution would be xor just the elements in odd indexes.
#     """
#     if len(arr) % 2 == 0:
#         result = 0
#     else:
#         result = 0
#         for index in range(0, len(arr)):
#             if index % 2 == 0:
#                 result ^= arr[index]
#
#     return result
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     t = int(input().strip())
#
#     for t_itr in range(t):
#         n = int(input().strip())
#
#         arr = list(map(int, input().rstrip().split()))
#
#         result = sansaXor(arr)
#
#         fptr.write(str(result) + '\n')
#
#     fptr.close()
