#!/bin/python3
#https://www.hackerrank.com/challenges/three-month-preparation-kit-divisible-sum-pairs/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one
import math
import os
import random
import re
import sys


def get_reminders(ar: list, k: int):
    '''
    gets the reminders of the items in an array when k is provided. Organize values according their reminders
    '''
    reminders = {}

    for index, value in enumerate(ar):
        if value % k not in reminders.keys():
            reminders[value % k] = [index]
        else:
            reminders[value % k].append(index)
    return reminders


def divisibleSumPairs(n, k, ar):
    residuo = get_reminders(ar, k)
    count = 0
    for index, values in enumerate(ar):
        if index < len(ar) - 1:
            modulo = values % k
            reminder = k - modulo if modulo != 0 else 0
            if reminder in residuo:
                for i in residuo[reminder]:
                    if index < i:
                        count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


