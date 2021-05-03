# https://www.hackerrank.com/challenges/priyanka-and-toys/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#
'''
Sample Input

8
# https://www.hackerrank.com/challenges/priyanka-and-toys/problem1 2 3 21 7 12 14 21

Sample Output

4
'''

def toys(w):
    # Write your code here
    arr = sorted(w)
    first_value = arr[0]+4
    count = 1
    print(arr)
    for i in range(0, len(arr)-1):
        print(first_value,arr[i])
        if (first_value) < arr[i+1]:
            print(first_value, arr[i+1], "move")
            count += 1
            first_value = arr[i+1]+4

    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
