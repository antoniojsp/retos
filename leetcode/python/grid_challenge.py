#!/bin/python3
# https://www.hackerrank.com/challenges/three-month-preparation-kit-grid-challenge/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-five
import math
import os
import random
import re
import sys


#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
def check_alphabetic_in_order(arr) -> bool:
    """
    (list -> bool)
    Gets a list of letters and check if it's in alphabetic order
    """
    for index in range(0, len(arr) - 1):
        current = ord(arr[index])
        next_element = ord(arr[index + 1])
        if current > next_element:
            return False
    return True


def transpose(arr):
    """
    pythonic way than:  *zip(*arr)
    """
    i, j = 0, 0
    temp = []
    result = []
    while j < len(arr[i]):
        temp.append(arr[i][j])
        i += 1
        if i >= len(arr):
            i = 0
            j += 1
            result.append(temp)
            temp = []
    return result


def sort_row(arr):
    result = []
    for i in arr:
        temp = sorted(list(i))
        result.append(temp)
    return result


def gridChallenge(grid):
    # Write your code her
    temp = sort_row(grid)
    # print(temp)
    transpose_array = transpose(temp)
    # print(transpose_array)

    for i in transpose_array:
        if not check_alphabetic_in_order(i):
            return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()

# def check_alphabetic_in_order(arr) -> bool:
#     """
#     (list -> bool)
#     Gets a list of letters and check if it's in alphabetic order
#     """
#     for index in range(0, len(arr)-1):
#         current = ord(arr[index])
#         next_element = ord(arr[index+1])
#         if current > next_element:
#             return False
#
#     return True
#
#
#
#
# # a = ["a", "d", "e", "a"]
#
# # print(check_alphabetic_in_order(a))
#
#
# a = [["a","b","c","x"],
#      ["e","c","d","c"],
#      ["x","s","a","g"]]
# # print(*zip(*a))
#
# # i, j = 0, 0
# # temp = []
# # result = []
# # while j < len(a):
# #     temp.append(a[i][j])
# #
# #     i += 1
# #     if i >= len(a):
# #         i = 0
# #         j += 1
# #         result.append(temp)
# #         temp = []
#
# i, j = 0, 0
# temp = []
# result = []
# while j < len(a[i]):
#     temp.append(a[i][j])
#     size = len(a[i])
#     i += 1
#
#     if i >= len(a):
#         i = 0
#         j += 1
#         result.append(temp)
#         temp = []
#
#     # if j >= size:
#     #     break
#
# print(result)
