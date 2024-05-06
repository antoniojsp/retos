#!/bin/python3
# https://www.hackerrank.com/challenges/three-month-preparation-kit-counter-game/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-six
import math
import os
import random
import re
import sys
from math import sqrt, log2, floor


#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Write your code here
    turn = 0
    L = "Louise"
    R = "Richard"
    while True:
        close = floor(log2(n))
        power_of_two = (2 ** close)

        if power_of_two == n:
            n /= 2
        else:
            n -= power_of_two

        if n == 1:
            break
        turn += 1

    return L if turn % 2 == 0 else R


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
