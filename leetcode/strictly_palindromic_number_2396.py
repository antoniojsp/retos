from math import floor
test = 100


def convert_base(num:int, base):
    result = ""
    while 1 < num:
        reminder = num % base
        num /= base
        result += str(floor(reminder))

    return result[::-1]


print(convert_base(100,3))
