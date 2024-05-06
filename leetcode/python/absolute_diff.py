#!/bin/python3
#https://www.hackerrank.com/challenges/three-month-preparation-kit-minimum-absolute-difference-in-an-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-four
import math
import os
import random
import re
import sys


#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    min_diff = float('inf')
    for i in range(0, len(arr) - 1):
        current = abs(arr[i] - arr[i + 1])
        if current < min_diff:
            min_diff = abs(arr[i] - arr[i + 1])
    # Version with enumerate. Needs messy limit variable to stop the loop
    # limit = len(arr) - 2
    # for i, j in enumerate(arr):
    #     current = abs(j - arr[i+1])
    #     if current < min_diff:
    #         min_diff = current
    #     if i == limit:
    #         break

    return min_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
