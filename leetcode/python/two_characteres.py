#https://www.hackerrank.com/challenges/three-month-preparation-kit-two-characters/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-nine

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

from itertools import combinations

def remove_duplicates_consecutive(string:str):
    temp = string
    i = 1
    while i < len(temp):
        if temp[i-1] == temp[i]:
            temp = temp.replace(temp[i], "")
            i = 0
        i+=1
    return temp

def comb(string:str):
    return list(combinations(set(string), 2))

def is_valid(string:str):
    size = len(string)
    left = ""
    right = ""
    chars = list(set(string))
    for i in range(size):
        if i%2==0:
            left += chars[0]
            right += chars[1]
        else:
            left += chars[1]
            right += chars[0]
    return left == string or right == string

def possible_outcome(string:str, arr:list):
    result = []
    for combi in arr:
        temp = ""
        for i in string:
            if i in combi:
                temp += i
        if is_valid(temp):
            result.append(temp)
    return result

max_length = lambda x: len(x) if x is not None else 0

def alternate(s):
    # Write your code here
    first = remove_duplicates_consecutive(s)
    combination_list = comb(first)
    resultados = possible_outcome(first,combination_list)
    temp = list(map(max_length, resultados))
    return max(temp) if temp else 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
