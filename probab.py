import random as r

suma = 0
times = 200000
for _ in range(times):
    suma += r.randrange(0,2)

print(suma/times)