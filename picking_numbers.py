#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def isAbsoluteValueDiffRight(first_value, second_value):
    absolute_difference = abs(first_value - second_value)
    return absolute_difference == 0 or absolute_difference == 1


def pickingNumbers(a):
    # Write your code here
    a.sort()
    dictionary_values = {}
    for valueArr in a:
        if valueArr in dictionary_values:
            dictionary_values[valueArr] += 1
        else:
            dictionary_values[valueArr] = 1

    uniqueValues = list(dictionary_values)

    if len(uniqueValues) == 1:  # Case array is filled up with the same unique value
        return dictionary_values[uniqueValues[0]]

    maxDiffSoFar = 0
    i = 0
    while i < len(dictionary_values) - 1:
        current_value = uniqueValues[i]
        next_value = uniqueValues[i + 1]
        if isAbsoluteValueDiffRight(current_value, next_value):
            maxDiffSoFar = max(maxDiffSoFar, dictionary_values[current_value] + dictionary_values[next_value])
            i += 2
        else:
            maxDiffSoFar = max(maxDiffSoFar, dictionary_values[current_value])
            i += 1

    return maxDiffSoFar

    # version using list.
    # a.sort()
    # current_value = a[0]
    # count = 0
    # maximoSoFar = 0
    # for value in a:
    #     if isAbsoluteValueDiffRight(value, current_value):
    #         count += 1
    #         maximoSoFar = max(maximoSoFar, count)
    #     else:
    #         maximoSoFar = max(maximoSoFar, count)
    #         current_value = value
    #         count = 1

    # return maximoSoFar


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
