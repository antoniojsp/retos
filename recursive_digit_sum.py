#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
# https://www.hackerrank.com/challenges/three-month-preparation-kit-recursive-digit-sum/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-six

def superDigit(n: str, k: int) -> int:
    # Write your code here
    if len(n) == 1:
        return int(n)

    sum_digits = 0
    for digit in n:
        sum_digits += int(digit)

    result = str(sum_digits)
    return superDigit(result, len(result))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
