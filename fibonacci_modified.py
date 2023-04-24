
def fibonacciModified(t1, t2, n):
    # Write your code here
    for i in range(2, n):
        temp = t1 + t2**2
        t1, t2 = t2, temp
    return temp


print(fib(5))