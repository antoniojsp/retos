

def best_sum_tab(target, nums):

    table = [None for i in range(target+1)]
    table[0] = []

    for i in range(target+1):
        if table[i] is not None:
            for val in nums:



    print(table)


print(best_sum_tab(8,[2,3,5]))

# []none none none
# [2,2,2,2][2,3,3][3,5]u