def fun(a,b):
    if a < 9 or b > 5:
        return a + fun(b, a)

    return a + 2


print(fun(2, 9))
