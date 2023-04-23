
from math import sqrt, ceil
def sieve(n):
    integers = [True for _ in range(0, n+1)]
    integers[0], integers[1] = False, False

    for i in range(ceil(sqrt(len(integers)))):
        if integers[i]:
            for j in range(i*i, len(integers), i):
                integers[j] = False

    return [index for index, is_prime in enumerate(integers) if is_prime]

print(sieve(100000000))