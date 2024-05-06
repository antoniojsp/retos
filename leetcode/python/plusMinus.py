#https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    lenght = len(arr)
    # Runtime is o(n) since it has to check every element in the array to know if it's positive or negative
    for i in arr:
        if i > 0:
            positive+= 1
        elif i < 0:
            negative+= 1
        else:
            zero+= 1

    print(positive/lenght)
    print(negative/lenght)
    print(zero/lenght)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
