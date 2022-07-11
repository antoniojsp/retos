#!/bin/python3
# https://www.hackerrank.com/challenges/three-month-preparation-kit-angry-children/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-five
import math
import os
import random
import re
import sys


#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

class Minimum:
    def __init__(self):
        self.current_min = float('inf')

    def add(self, val):
        if val < self.current_min:
            self.current_min = val

    def __str__(self):
        return str(self.current_min)


def maxMin(k, arr):
    # Write your code here
    sorted_array = sorted(arr)
    result_diff = Minimum()
    minimum_subarray_index = 0
    maximum_subarray_index = len(sorted_array) - k + 1
    for index in range(minimum_subarray_index, maximum_subarray_index):
        lower = sorted_array[index]
        higher = sorted_array[index + k - 1]
        result_diff.add(higher - lower)

    return result_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
