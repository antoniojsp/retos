#!/bin/python3
#https://www.hackerrank.com/challenges/three-month-preparation-kit-dynamic-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-five
import math
import os
import random
import re
import sys


#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
def formula(x, lastAnswer, n):
    return (x ^ lastAnswer) % n


def dynamicArray(n, queries):
    # Write your code here
    storage2d = [[] for i in range(n)]
    lastAnswer = 0
    result = []
    for query, x_value, y_value in queries:
        if query == 1:
            idx = formula(x_value, lastAnswer, n)
            storage2d[idx].append(y_value)
        elif query == 2:
            idx = formula(x_value, lastAnswer, n)
            sizeStorageArrayIndexIdx = len(storage2d[idx])
            lastAnswer = storage2d[idx][y_value % sizeStorageArrayIndexIdx]
            result.append(lastAnswer)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
