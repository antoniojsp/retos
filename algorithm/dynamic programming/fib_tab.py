

def fib_tab(n):
    table = [0]*(n+1)
    table[1] = 1
    for i in range(2, (n+1)):
        table[i] = table[i-1] + table[i-2]
    return table[-1]

def fib_i(n):
    a = 0
    b = 1
    for _ in range(n-1):
        print(a, b)
        temp = a + b
        a = b
        b = temp

    return b


