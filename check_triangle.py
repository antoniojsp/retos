# https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
#!/bin/python3

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
def check_triangle(arr):
    #gets list with 3 sides and checks if exists
    a = arr[0]
    b = arr[1]
    c = arr[2]
    
    if a+b>c and a+c>b and b+c>a:
        return True
    else: 
        return False
        
def maximumPerimeterTriangle(sticks):
    # Write your code here
    arr = sorted(sticks, reverse=True)
    for i in range(len(arr)-2):
        if check_triangle([arr[i], arr[i+1], arr[i+2]]):
            return arr[i+2], arr[i+1],arr[i] 

    return [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
