#!/bin/python3
#https://www.hackerrank.com/challenges/three-month-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one
import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    partes = s.split(":")
    AM_PM = True if partes[2][2] == "P" else False #check for afternnon or morning
    hour = partes[0]

    if AM_PM:
        if hour != "12":
            hours_str = str(int(hour) + 12)
            partes[0] = hours_str
    else:
        if hour == "12":
            partes[0] = "00"

    return ":".join(partes)[:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
