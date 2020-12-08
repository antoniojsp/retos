#!/bin/python3
#https://www.hackerrank.com/challenges/missing-numbers/problem
import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):

    dict1 = {}
    for i in arr:
        dict1[i] = 0
    dict2 ={}
    for i in brr:
        dict2[i] = 0

    for i in arr:
        dict1[i] += 1

    for i in brr:
        dict2[i] += 1

    lista = []

    for i in dict2.keys():
        if i not in dict1.keys():
            lista.append(int(i))
        elif dict2[i] > dict1[i]:
            lista.append(int(i))

    return sorted(lista)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
