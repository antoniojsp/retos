#https://www.hackerrank.com/challenges/three-month-preparation-kit-caesar-cipher-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-four
# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
def CharValueInRange(character :chr) -> int:
    '''
    (char->int)
    Gets a char and returns its int value in range from 0 to 25 (26 letter of alphabet)
    '''
    lowerAsciiStarIndex = ord("a")
    charAsciiValue = ord(character.lower())
    return charAsciiValue - lowerAsciiStarIndex

def cipheredChar(value :int, shift: int) -> int:
    '''
    Gets an int that represents the order of the character in the alphabet and swift it "shift" times.
    '''
    sizeOfEnglishAlpahabet = 26  # if Spanish is used, it would need 27 character to represent all the alphabet
    return int(value + shift) % sizeOfEnglishAlpahabet

def caesarCipher(s, k) -> str:
    # Write your code here
    result = ""
    for character in s:
        char_int = CharValueInRange(character)
        ciphered_char = cipheredChar(char_int, k)
        upper, lower = ord("A"), ord("a")

        if not character.isalpha():
            result += character
        elif character.isupper():
            result += chr(ciphered_char + upper)
        else:
            result += chr(ciphered_char + lower)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()



'''
index + shift
1 + 10 : 11 % 26 = 11 -> a -> l
15 + 23 : 38 % 26 = 12 -> 


'''

# def CharValueInRange(character:chr) -> int:
#     '''
#     (char->int)
#     Gets a char and returns is int value in range from 0 to 25 (26 letter of alphabet)
#     '''
#
#     result, firstUpperChr, firstLowerChr = 0, 65, 97
#     characterAsciiValue = ord(character)
#     if character.isupper():
#         result = characterAsciiValue - firstUpperChr
#     else:
#         result = characterAsciiValue - firstLowerChr
#
#     return result
#
#
# s = "middle-Outz"
# shift = 2
# result = ""
# for i in s:
#     value = CharValueInRange(i)
#     new_value = int(value + shift) % 26
#     upper, lower = 65, 97
#
#     if not i.isalpha():
#         result += i
#     elif i.isupper():
#         result += chr(new_value + upper)
#     else:
#         result += chr(new_value + lower)

print(result)


