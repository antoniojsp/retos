test = [1,100,1,1,1,100,1,1,100,1]

def cost_climbing_stairs(arr):

    def helper(cost, count):

        if count > len(cost)+1:
            return 0
        if count == len(cost)+1:
            return 1

        return min(helper(cost, count-1) + cost[count-1], helper(cost, count-2) + cost[count-2])



    return helper(arr, 0)





# def cost_climbing_stairs(arr):
#
#     def helper(cost):
#
#         if len(cost) == 1:
#             return 0
#         elif len(cost) == 2:
#             return min(cost[0], cost[1])
#         else:
#             cost_1 = cost[-1] + helper(cost[:-1])
#             cost_2 = cost[-2] + helper(cost[:-2])
#             return min(cost_1, cost_2 )
#
#
#     return helper(arr)

print(cost_climbing_stairs(test))