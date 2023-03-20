def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False

# print(is_palindrome(6345436))
def infinite_sequence():
    num = 0
    while True:
        num += 1
        yield num

import random
def infinite_sequence_random(num=None):
    while True:
        num.append(random.randint(0,10))
        yield num

for i in range(0,10):
    print(next(infinite_sequence_random([])))

# for i in infinite_sequence():
#     pal = is_palindrome(i)
#     if pal:
#         ...
#         print(i)