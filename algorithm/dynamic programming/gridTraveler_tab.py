from pprint import pprint
def grid_trav(row, col):

    table = [[0 for i in range(row+1)]for i in range(col+1)]
    table[1][1] = 1

    for i in range(row+1):
        for j in range(col+1):
            if i+1 < col+1:
                table[i+1][j] += table[i][j]
            if j+1 < row+1:
                table[i][j+1] += table[i][j]
    return table[row][col]


pprint(grid_trav(3, 3))

