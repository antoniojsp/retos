# https://www.hackerrank.com/challenges/three-month-preparation-kit-closest-numbers/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-four
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr.sort()  # put next to each other the values according to it's value so the minimum diff is between one index to the next one
    dictionary_diff = {}

    for i in range(0, len(arr) - 1):
        substraction = abs(arr[i] - arr[i + 1])
        # print(arr[i], arr[i+1], substraction)
        if substraction not in dictionary_diff:
            dictionary_diff[substraction] = [(arr[i], arr[i + 1])]
            # dictionary_diff[substraction] = [arr[i], arr[i+1]]

        else:
            dictionary_diff[substraction].append(((arr[i], arr[i + 1])))
            # dictionary_diff[substraction] += [arr[i], arr[i+1]]
        # print(dictionary_diff)

    minimum = min(dictionary_diff.keys())
    return [x for i in dictionary_diff[minimum] for x in i]
    # return dictionary_diff[minimum]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
