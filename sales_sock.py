# https://www.hackerrank.com/challenges/three-month-preparation-kit-sock-merchant/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-three

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    dictionary = {}
    result = 0
    for i in ar:
        if i not in dictionary:  # add new key if color is not in dictioonary
            dictionary[i] = 1
        else:  # add up count in the key and check if it's a pair.
            dictionary[i] += 1
            if dictionary[i] % 2 == 0:
                dictionary[i] -= 2
                result += 1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
