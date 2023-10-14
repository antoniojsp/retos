test = [10,15,20]

def cost_climbing_stairs(arr):

    def helper(stairs_cost, count):

        if count <= 0:
            return stairs_cost[0]
        if count == 1:
            return stairs_cost[1]

        return min(helper(stairs_cost, count-1) + stairs_cost[count] , helper(stairs_cost, count-2) + stairs_cost[count])


    return helper(arr, len(test)-1)

print(cost_climbing_stairs(test))