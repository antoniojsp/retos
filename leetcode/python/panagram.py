#https://www.hackerrank.com/challenges/three-month-preparation-kit-pangrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-two

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# def create_abc_dict(start:chr, end:chr):
#     '''
#     Creates a dictionary that have as keys chars from a range selected using the ASCII table.
#     '''
#     return {chr(i):0 for i in range(ord(start), ord(end)+1) if str(chr(i)).isalpha()}
def create_string_abc(start, end):
    abc = ""
    for i in range(ord(start), ord(end) + 1):
        abc += chr(i)
    return abc


def pangrams(s):
    # dictionary = create_abc_dict("a", "z")
    stringa = create_string_abc('a', 'z')
    for i in stringa:
        if i not in s.lower() and i != ' ':
            return "not pangram"

    return "pangram"

    # for i in s:
    #     if i != " ":
    #         dictionary[str(i).lower()] += 1

    # if 0 in dictionary.values():
    #     return "not pangram"

    # return "pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

