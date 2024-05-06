#!/bin/python3
# https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=false
import math
import os
import random
import re
import sys
from math import sqrt, ceil, floor


#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s: str) -> str:
    square_root_lenght = sqrt(len(s))
    number_rows = floor(square_root_lenght)
    number_columns = ceil(square_root_lenght)
    result = ""

    for i in range(number_columns):
        for j in range(i, len(s), number_columns):
            result += s[j]
        result += " "

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
