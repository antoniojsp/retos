def minimumNumber(n:int, password:str)->int:
    length = 6 - len(password)

    counter = {"digits":0, "lower":0, "upper":0, "special":0}

    for i in password:
        if i in "0123456789":
            counter["digits"]+=1
        elif i in "abcdefghijklmnopqrstuvwxyz":
            counter["lower"]+=1
        elif i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            counter["upper"]+=1
        elif i in "!@#$%^&*()-+":
            counter["special"]+=1

    needing = sum(1 for i in counter.values() if i == 0)

    return max(length, needing)

test = "#HackerRank"
# print(minimumNumber(0, test))

import re

test = "#HackerRank"
lower = re.findall('[a-z]', test)
upper = re.findall('[A-Z]', test)
digits = re.findall('[0-9]', test)
special = re.findall('[!@#$%^&*()-+]', test)

def minimumNumber(n:int, password:str)->int:
    length = 6 - len(password)
    print(length)
    counter = {"lower": len(re.findall('[a-z]', password)),
               "upper": len(re.findall('[A-Z]', password)),
               "digits": len(re.findall('[0-9]', password)),
               "special": len(re.findall('[!@#$%^&*()+-]', password))}
    print(counter)
    needing = sum(1 for i in counter.values() if i == 0)

    return max(length, needing)


print(minimumNumber(0, "AUzs-nV"))



#!/bin/python3
#https://www.hackerrank.com/challenges/three-month-preparation-kit-strong-password/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-five
import math
import os
import random
import re
import sys


#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

# def checkDigit(password:str):
#     numbers = "0123456789"
#     for i in numbers:
#         if str(i) in password:
#             return True
#     return False

# def checkUpper(password:str):
#     lower = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     for i in lower:
#         if i in password:
#             return True
#     return False

# def checkLower(password:str):
#     upper = "abcdefghijklmnopqrstuvwxyz"
#     for i in upper:
#         if i in password:
#             return True
#     return False

# def checkSpecial(password:str):
#     special_characters = "!@#$%^&*()-+"
#     for i in special_characters:
#         if i in password:
#             return True
#     return False
#
# def checkCondition(password: str, conditions: str):
#     return any(True if i in password else False for i in conditions)
#
#
# def minimumNumber(n, password):
#     lenghtPassword = len(password)
#     howShortPassword = 6 - lenghtPassword
#
#     # functions = [checkDigit, checkLower, checkSpecial, checkUpper]
#     # count = 0
#     # for func in functions:
#     #     if not func(password):
#     #       count += 1
#
#     conditions = ["0123456789", "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "!@#$%^&*()-+"]
#
#     result = [checkCondition(password, i) for i in conditions]
#     return max(howShortPassword, result.count(False))
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input().strip())
#
#     password = input()
#
#     answer = minimumNumber(n, password)
#
#     fptr.write(str(answer) + '\n')
#
#     fptr.close()
