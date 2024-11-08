#!/bin/python3
#https://www.hackerrank.com/challenges/three-month-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def sum_list(arr, s, e):
    '''
    Function will sum the elements from index 's' to index 'e'
    '''
    result = 0
    for i in range(s,e):
        result+=arr[i]

    return result

def miniMaxSum(arr):

    '''
    Runtime is 0(n) since it has to touch every single element in the array. It timers need to sort it and then just add all the elements but the timers for the maximum and all the elements but the timers for the minimum
    '''

    en_orden = sorted(arr)

    maximo = sum_list(en_orden, 1, 5)
    minimo = sum_list(en_orden, 0, 4)

    print(minimo, maximo)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
