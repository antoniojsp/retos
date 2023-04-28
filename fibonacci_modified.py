
def fibonacciModified(t1, t2, n):
    # Write your code here
    next_t = 0
    for i in range(2, n):
        next_t = t1 + t2**2
        t1, t2 = t2, next_t
    return next_t


print(fibonacciModified(0,1 ,5))