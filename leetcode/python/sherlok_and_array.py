#!/bin/python3
# https://www.hackerrank.com/challenges/three-month-preparation-kit-sherlock-and-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-six
import math
import os
import random
import re
import sys


#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr: list) -> str:
    # Write your code here
    right_side = sum(arr)
    left_side = 0
    for center_value in arr:
        right_side -= center_value
        if left_side > right_side:
            return "NO"
        elif right_side == left_side:
            return "YES"
        left_side += center_value

    # BRUTE FORCE!!!
    # for i in range(0, len(arr)):
    #     if sum(arr[:i]) == sum(arr[i+1:]) :
    #         return "YES"
    # return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
