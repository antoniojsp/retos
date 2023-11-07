def getWays(n, c):
    def helper(target, coins, memo={}):

        if target == 0:
            return 1
        if target < 0:
            return 0

        if (target, len(coins)) in memo:
            return memo[(target, len(coins))]

        total = 0
        for i in range(len(coins)):
            coin = coins[i]
            if coin > target:
                continue
            else:
                total += helper(target - coins[i], coins[i:], memo)

        memo[(target, len(coins))] = total

        return memo[(target, len(coins))]

    return helper(n, c)


print(getWays(4, [1, 2, 3]))