#https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
#!/bin/python3

import math
import os
import random
import re
import sys

def return_dict(string):
    lista = {}
    for i in range(0,26):
        lista[str(chr(i+97))] = 0
    
    for i in string:
        lista[i] += 1
        
    return lista

def return_index(string):
    lista = [0]*26
    for i in string:
        lista[ord(i)-97] += 1
    return lista
def restar_listas(a, b):
    resultado = [0]*26
    
    for i in range(len(a)):
        resultado[i] = abs(a[i]-b[i])
        
    return resultado

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    primero = return_index(a)
    segundo = return_index(b)    
    suma = 0
    for i in restar_listas(primero,segundo):
        suma+= i
    return suma
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
