def gcd(a, b) -> int:
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

print(gcd(6,18))