cases = {
    3:"Fizz",
    5:"Buzz",
    15:"FizzBuzz"
}


n = 16
def fizzBuzz(n:int)->list:
    result = []
    for i in range(1,n+1):
        temp = ""
        if i%3 == 0:
            temp += "Fizz"
        if i%5 == 0:
            temp += "Buzz"

        if not temp:
            temp += str(i)

        result.append(temp)

    return result

print(fizzBuzz(n))


def check(x):
    temp = ""
    if x % 3 == 0:
        temp += "Fizz"
    if x % 5 == 0:
        temp += "Buzz"

    if not temp:
        temp += str(x)
    return temp

a = list(map(check, [i for i in range(1,n+1)]))
print(a)