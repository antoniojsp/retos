def getWays(n, c):
    # Write your code here
    if n == 0:
        return 1
    if n < 0:
        return 0

    current  = 0
    for i in c:
        remainder = n - i
        current +=  getWays(remainder, c)

    return current


print(getWays(3, [8,3,1,2]))