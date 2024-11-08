from math import ceil, sqrt

SIZE_ARRAY_MULTIPLIER = 15 # random variable hoping that the n timers primes are inside that range

def re_stack(source, destination):
    for _ in range(len(source)):
        destination.append(source.pop())


def sieve_position(n):
    integers = [True for _ in range(0, SIZE_ARRAY_MULTIPLIER*n+1)]
    integers[0], integers[1] = False, False
    count = 0
    for i in range(ceil(sqrt(len(integers)))):
        if integers[i]:
            for j in range(i*i, len(integers), i):
                integers[j] = False
                count += 1

    return [index for index, is_prime in enumerate(integers) if is_prime][:n]

def waiter(number, q):
    primes = sieve_position(q)
    answer = []
    for index, prime in enumerate(primes):
        current_prime = prime
        b = []
        a_i = []
        for _ in range(len(number)):
            top = number.pop()
            if top % current_prime == 0:
                b.append(top)
            else:
                a_i.append(top)
        re_stack(b, answer)
        number = a_i
    else:
        re_stack(number, answer)

    return answer

print(waiter([2,3,4,5,6,7], 3))

#primes
from math import sqrt


# Function check whether a number
# is prime or not
def isPrime(n):
    # Corner case
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def primes(n):
    answer = [2,3]
    count = 0
    i = 0
    while len(answer) < n:
        if isPrime(6*i-1):
            answer.append(6*i-1)
            count +=1
        if isPrime(6*i+1):
            answer.append(6*i+1)
            count +=1
        i +=1
    return answer






