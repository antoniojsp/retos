#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(num: str):
    candidate = ""
    for i in range(1, (len(num) // 2) + 1):
        value = int(num[:i])
        first_value = value
        while len(candidate) < len(num):  # generates possible result
            candidate += str(value)
            value += 1

        if num == candidate:  # check if candidate is equal to the string provided
            print("YES", first_value)
            return
        else:
            candidate = ""  # reset and check again
    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
