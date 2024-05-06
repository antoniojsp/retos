#!/bin/python3
# https://www.hackerrank.com/challenges/lisa-workbook/problem?isFullScreen=true
import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n,k, arr):
    page = 1
    count_special = 0

    for chapter in arr:
        number_of_problems = chapter
        for problem_number in range(1, number_of_problems+1):
            if page == problem_number: # check if it's special
                count_special +=1
            if problem_number == chapter: # break loop once reach the last problem
                break
            if problem_number%k == 0: # if need to pass page.
                page +=1
        page +=1

    return count_special

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
