k = 3
maximum = 10
multiples = [i*k for i in range(1, maximum) if i*k <= maximum]
arr = [1, 3, 2, 6, 1, 2]
dict_arr = {i: 0 for i in arr}
print(dict_arr)
print(multiples)
# c = {4: 0, 8: 0, 12: 0, 16: 0, 20: 0}
# a + b = c
# c % k = 0
# a = c - b

# 4 = 1 + 1
# 4 = 1 + 2
# 4 = 1 + 3
# 4 = 1 + 4
value = 0
for i in sorted(arr):
    print(i, "value")
    for j in multiples:
        temp = abs(j - i)
        if temp in dict_arr:
            if temp != i and temp < i:
                value += 1
                print(str(temp) + " + " + str(i) + " = " + str(j))
