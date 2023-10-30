def getWays(n, c):
    # Write your code here
    def helper(target, coins):

        if target == 0:
            return 1

        if val > 0:
            return 0
        result = 0
        for i in arr:
            result += helper(val - i)

        return result

    return helper(n, c)


print(getWays(3,[8,3,1,2]))





