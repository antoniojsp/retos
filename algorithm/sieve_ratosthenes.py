
from math import sqrt, ceil, floor
def sieve(n):
    integers = [True for _ in range(0, n+1)]
    integers[0], integers[1] = False, False
    count = 0
    for i in range(ceil(sqrt(len(integers)))):
        if integers[i]:
            for j in range(i*i, len(integers), i):
                count +=1
                integers[j] = False


    return [i for i in range(len(integers)) if integers[i]]

print(sieve(1000))