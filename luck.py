#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    suma = 0
    temp = sorted(contests, reverse=True)
    limit = 0
    for i in range(len(temp)):
        if temp[i][1] == 1 and limit < k:
            suma+=temp[i][0]
            limit+=1
        elif temp[i][1] == 1 and limit >= k:
            suma-=temp[i][0]
        elif temp[i][1] == 0:
            suma+=temp[i][0]
        
    return suma 
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
