"""
How many ways we can climb a stair?

we can take one step or two steps
n = number of steps
"""

n = 5

def climbing_stairs(stairs):  # dynamic programming, memoization

    def helper(n, count, seen = {}):
        if count in seen:
            return seen[count]
        if count > n:
            return 0
        if count == n:
            return 1
        seen[count] = helper(n, count+1) + helper(n, count+2)
        return seen[count]

    return helper(stairs, 0)


# print(climbing_stairs(5))

def climbing_stairs2(stairs):

    partial_results = [0]*(stairs + 1)

    partial_results[stairs-1], partial_results[stairs] = 1, 1  # base case is the last stair and it will always be one.
    # the previous step to the end one, we can only go one step, since taking 2 takes out of the stairs.

    for i in range(stairs-2, -1, -1):  # since we already have the answer of the last 2 steps, we can calculate the
        #previous step by adding up the two next steps from any index < ending-1. We calculate them by going backwards.
        partial_results[i] = partial_results[i+1] + partial_results[i+2]

    return partial_results[0] # once we reach the zero index, we return its contains.

print(climbing_stairs2(3))
