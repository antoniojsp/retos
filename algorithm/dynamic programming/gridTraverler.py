

def grid_traveler(row, col, memo = {}):
    name = f"{row}, {col}"
    if name in memo:
        return memo[name]
    if row == 1 and col == 1:
        return 1
    if row == 0 or col == 0:
        return 0

    memo[name] = grid_traveler(row-1, col, memo) + grid_traveler(row, col-1, memo)
    return memo[name]





print(grid_traveler(18,18))