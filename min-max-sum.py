#!/bin/python3

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
    Runtime is 0(n) since it has to touch every single element in the array. It first need to sort it and then just add all the elements but the first for the maximum and all the elements but the first for the minimum
    '''

    en_orden = sorted(arr)

    maximo = sum_list(en_orden, 1, 5)
    minimo = sum_list(en_orden, 0, 4)

    print(minimo, maximo)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
