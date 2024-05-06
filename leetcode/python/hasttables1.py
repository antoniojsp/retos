#!/bin/python3
#https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    val = True
    magazine_dict = {}
    note_dict = {}
    zero = 0

    for i in magazine:
        magazine_dict[i] = 0
    for i in note:
        note_dict[i] = 0

    for i in magazine:
        magazine_dict[i] = magazine_dict[i] + 1
    for i in note:
        note_dict[i] = note_dict[i] + 1

    for i in note_dict:
        if i in magazine_dict.keys():
            if note_dict[i]<=magazine_dict[i]:
                val = True
            else:
                val = False
                break
        else:
            val = False
            break

    if val:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
