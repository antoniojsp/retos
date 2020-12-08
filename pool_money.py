#https://www.hackerrank.com/challenges/icecream-parlor/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    result = []

    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[i]+arr[j] == m and i != j:
                result.append(i+1)
                result.append(j+1)
                break

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
