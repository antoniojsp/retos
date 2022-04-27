#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/three-month-preparation-kit-kangaroo/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-four
#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    # if v2 - v1 == 0: # Division by Zerp, means no solution
    #     return "NO"

    ratio = float(x2 - x1) / (v2 - v1) if v2 - v1 != 0 else 1

    # if ratio is negative, at some point, those two would meet, otherwise, they will separate forever
    # ratio would be set to a value if v2- v1 is not zero, since division by zero is infinite. If that's case. ratio is set at 1 and return "NO"

    if ratio <= 0 and ratio.is_integer():
        return "YES"
    else:
        return "NO"

    # BRUTE FORCE
    # for i in range(0,2000000):
    #     if 0 == i*(v2 - v1) + (x2 - x1):
    #         print(i)
    #         return "YES"
    # return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
