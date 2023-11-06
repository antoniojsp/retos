def getWays(n, c):
    # Write your code here
    result = 0
    def helper(target, coins):

        if target == 0:
            return 1
        if target > 0:
            return 0
        for i in coins:
            result+= 3

        return result

    return helper(n, c)


print(getWays(3,[8,3,1,2]))





