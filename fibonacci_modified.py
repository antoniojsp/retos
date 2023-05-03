
def fibonacciModified(t1, t2, n):
    # Write your code here
    next_t = 0
    for i in range(2, n):
        next_t = t1 + t2**2
        t1, t2 = t2, next_t
    return next_t


print(fibonacciModified(0,1 ,5))

def fibo(num, cache):
    print(cache)
    if cache[num] == -1:
        cache[num] = fibo(num - 1, cache)+fibo(num -2, cache)

    return cache[num]

def fibo_launch(n):

    arr = [-1]*(n+1)
    arr[0], arr[1] = 1,1
    return fibo(n, arr)

print(fibo_launch(5000))
