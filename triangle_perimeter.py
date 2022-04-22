#!/bin/python3
#https://www.hackerrank.com/challenges/three-month-preparation-kit-maximum-perimeter-triangle/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-three
import math
import os
import random
import re
import sys


#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    arr = sorted(sticks)
    suma_max = 0
    resultado = None
    for i in range(0, len(arr) - 2):
        '''
        let's say
        1 2 3 4 5 6
        It's and ordered list with lenghts
        now
        A triangle is legal when, from sides a, b and c, we get
        a + b > c
        b + c >a
        a +c > b

        we say that index 0 and 1 are "a" and "b"
        if find "c" among the rest of the list that fullfill a + b > c, then we would have
        the rest of the rules to follow.

        if c is bigger than a + b
        and a < b < c
        We got that b + c > a since c is already bigger than a
        and  a + c > b since c is bigger than b
        '''
        # lados = []
        ab = arr[i] + arr[i + 1]
        for j in (range(i + 2, len(arr))):
            if ab > arr[j]:
                """
                if a+b > c, then we pack the three sides in one list. We sum it and compare with the current max
                """
                lados = [arr[i], arr[i + 1], arr[j]]
                if sum(lados) > suma_max:
                    resultado = lados

    if not resultado:
        return [-1]

    return resultado


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
