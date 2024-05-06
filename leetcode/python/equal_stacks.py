#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#
def arr_sums(arr: list) -> list:
    suma = 0
    result = []
    for i in arr:
        suma += i
        result.append(suma)
    return result


def equalStacks(h1, h2, h3):
    # Write your code here
    a1, a2, a3 = arr_sums(h1[::-1]), arr_sums(h2[::-1]), arr_sums(h3[::-1])
    result1 = set(a1)
    result2 = set(a2)
    result3 = set(a3)
    u = set.intersection(result1, result2, result3)

    result = 0
    if len(u) != 0:
        result = max(u)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
