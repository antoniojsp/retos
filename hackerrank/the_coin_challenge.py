
def getWays(n, c):
    # Write your code here
    def helper(value, arr:list):

        if value == 0:
            return 1

        return 1 + helper(value - 1, arr)

    return helper(n, c)


