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

def pickingNumbers(a):
    # Write your code here

    # using a dictionary to count the incidences of values in the array
    # a.sort()
    # dictionary_values = {}

    # for i in a:
    #     if i in dictionary_values:
    #         dictionary_values[i] += 1
    #     else:
    #         dictionary_values[i] = 1

    # # print(dictionary_values)
    # keys = list(dictionary_values)
    # i = 0
    # result = []

    # if len(keys) == 1: # if the array is filled up with the same unique value
    #     return dictionary_values[keys[0]]

    # maximo = 0
    # while i < len(keys)-1:
    #     if abs(keys[i] - keys[i+1]) == 1:
    #         maximo = max(maximo, dictionary_values[keys[i]] + dictionary_values[keys[i+1]])
    #         i+=2
    #     else:
    #         maximo = max(maximo, dictionary_values[keys[i]])
    #         i+=1

    # return maximo

    # version using list.
    a.sort()
    current_value = a[0]
    count = 0
    maximoSoFar = 0
    for value in a:
        absoluteDiff = value - current_value
        if absoluteDiff == 1 or absoluteDiff == 0:
            count += 1
            maximoSoFar = max(maximoSoFar, count)
        else:
            maximoSoFar = max(maximoSoFar, count)
            current_value = value
            count = 1

    return maximoSoFar


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
