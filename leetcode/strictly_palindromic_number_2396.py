from math import floor
test = 100


def convert_base(num:int, base) -> str:
    result = ""
    while 1 < num:
        reminder = num % base
        num /= base
        result += str(floor(reminder))

    return result[::-1]

def check_palindrome(num:str) -> bool:

    for i in range(0, len(num)//2):
        if num[i] != num[len(num)-i-1]:
            return False
    return True

print(check_palindrome("1000"))


# print(convert_base(100,3))
