#https://www.hackerrank.com/challenges/three-month-preparation-kit-countingsort4/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-five
# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def list_to_array(arr):
    result = ""
    for i in arr:
        result += i+ " "
    return result[:-1]


def counting_sort(arr) -> list:
    maxIndexValue = int(max(arr)[0]) + 1
    b = {i: [] for i in range(maxIndexValue)}
    for i in arr:
        b[int(i[0])].append(i[1])

    result = ""
    for i in b.values():
        if i:
            temp = list_to_array(i)
            result += temp + " "

    return result


def add_dash(arr) -> list:
    length = int(len(arr) / 2)
    for i in range(0, length):
        arr[i][1] = "-"
    return arr


def countSort(arr):
    temp = add_dash(arr)
    result = counting_sort(temp)
    print(result)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)

# arr =[['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['4', 'ij'], ['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['0', 'ij'], ['4', 'that'], ['3', 'be'], ['0', 'to'], ['1', 'be'], ['5', 'question'], ['1', 'or'], ['2', 'not'], ['4', 'is'], ['2', 'to'], ['4', 'the']]
#
# b = {i: [] for i in range(10)}
#
# def add_dash(arr)->list:
#     lenght = int(len(arr)/2)
#     for i in range(0, lenght):
#         arr[i][1] = "-"
#     return arr
# temp = add_dash(arr)
#
# for i in temp:
#     b[int(i[0])].append(i[1])
#
# for i in b.values():
#     temp = ' '.join(i)
#     print(temp, end=" ")
#
