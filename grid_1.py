# https://www.hackerrank.com/challenges/grid-challenge/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
def tranpose(arr):
    
    result = []*len(arr)
    
    i=0
    while i < len(arr):
        j = 0
        temp = []
        while j < len(arr):
            temp.append(arr[j][i])
            j+=1
        i+=1
        result.append(temp)
        
    return result
        

def gridChallenge(grid):
    # Write your code here
    alpha = [sorted(i)for i in grid]
    j = 0
    temp = tranpose(alpha)
    print(temp)
    for i in range(len(temp)):
        for j in range(len(temp)-1):
            if temp[i][j] > temp[i][j+1]:
                return "NO"
            
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
