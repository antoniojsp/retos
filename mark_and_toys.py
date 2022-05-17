#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#
def maximumToys(prices, k):
    # O(n)
    prices.sort()  # O(nlogn)
    suma = 0
    count = 0
    for i in prices:
        suma += i
        if suma <= k:
            count += 1
        else:
            break  # run out of money. Max number of gifts

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()