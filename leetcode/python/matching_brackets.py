#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def is_closed(open:str, close:str):
    brackets = {"{":"}", "(":")", "[":"]"}
    if brackets[open] == close:
        return True
    return False

def isBalanced(test:str):
    bracket = []

    for i in test:
        if i in ["(", "[", "{"]:
            bracket.append(i)
        elif i in [")", "]",  "}"]:
            if bracket:
                open = bracket.pop()
                if not is_closed(open, i):
                    return "NO"
            else:
                return "NO"

    return "YES" if not bracket else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
