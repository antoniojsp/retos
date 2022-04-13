# https://www.hackerrank.com/challenges/three-month-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def flat(arr):
    return [j for i in arr for j in i]


def diagonalDifference(arr):
    # Write your code here
    if not arr:
        return 0
    flat_list = flat(arr)
    lenght = len(arr)

    left, right = 0, 0

    for i, j in zip(range(0, len(flat_list), lenght + 1), range(lenght - 1, len(flat_list), lenght - 1)):
        left += flat_list[i]
        right += flat_list[j]

    # for i in range(0,len(flat_list)-1):
    #     left += flat_list[i+(i*lenght-1)]
    #     right += flat_list[(i+lenght-1)+(i*lenght-1)]

    return abs(left - right)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
