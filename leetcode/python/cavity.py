#https://www.hackerrank.com/challenges/cavity-map/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.

def cavityMap(grid):
    lenght = len(grid)
    if lenght > 2:
        temp = []
        for i in grid:
            for j in i:
                temp.append(j)


        for i in range(1, lenght-1):
            for j in range(1, lenght-1):
                if grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i+1][j] and \
                grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i][j+1]:
                    temp[i*lenght+j] = "X"

        result = []*lenght

        for i in range(0, lenght):
            linea = ""
            for j in range(0, lenght):
                linea += temp[i*lenght+j]
            result.append(linea)

        return result
    else:
        return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
