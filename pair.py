multiples = {}

k = 4
maximum = 200
for i in range(1, 6):
    if i*k > maximum:
        break
    multiples[k*i] = 0

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# c = {4: 0, 8: 0, 12: 0, 16: 0, 20: 0}
# a + b = c
# c % k = 0
# a = c - b

print(multiples)

