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


def sansaXor(arr):
    # Write your code here
    """
    if len(arr) is even, then getting all the posible combinations of subarrays would contain numbers in pairs. if it's odd, then the solution would be xor just the elements in odd indexes.
    """
    if len(arr) % 2 == 0:
        result = 0
    else:
        result = 0
        for index in range(0, len(arr)):
            if index % 2 == 0:
                result ^= arr[index]

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
