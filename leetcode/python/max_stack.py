#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#
class Stack:
    def __init__(self):
        self.stack = []
        self.max_lista = []

    def __repr__(self):
        return str(self.stack)

    def print(self):
        print("#### STATUS  #####")
        print(f"Stack {self.stack}")
        print(f"Max Lista {self.max_lista}")
        if self.max_lista:
            print(f"Maximo {self.max_lista[-1]}\n")
        else:
            print("Stack Empty\n")

    def push(self, val):
        self.stack.append(val)
        if self.max_lista:
            if self.max_lista[-1] < val:
                self.max_lista.append(val)
                self.maxi = val
            else:
                self.max_lista.append(self.max_lista[-1])
        else:
            self.max_lista.append(val)

    def maximum(self):
        if self.max_lista:
            return self.max_lista[-1]
        else:
            0

    def pop(self):
        self.max_lista.pop()
        self.stack.pop()


def getMax(operations):
    # Write your code here
    new_stack = Stack()
    result = []
    for i in operations:
        operation = i.split(" ")
        if int(operation[0]) == 1:
            new_stack.push(int(operation[1]))
        elif int(operation[0]) == 2:
            new_stack.pop()
        elif int(operation[0]) == 3:
            result.append(new_stack.maximum())

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
