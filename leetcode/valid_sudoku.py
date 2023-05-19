arr = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

from collections import Counter


def check(arr):
    for i in arr:
        temp = "".join(list(map(lambda x: x if x != "." else "", i)))
        seen = set()
        for j in temp:
            if j in seen:
                return False
            seen.add(j)

    for i in range(len(arr)):
        temp = []
        seen = set()
        for j in range(len(arr)):
            if arr[j][i] != ".":
                if arr[j][i] in seen:
                    return False
                seen.add(arr[j][i])
    return True

# print(check(arr))

for i in range(9):
    for j in range(9):
        if (j+1)%3 == 0:
            print(f"{arr[i][j]}      ", end="")
        else:
            print(f"{arr[i][j]} ", end="")

    if (i+1)%3==0:
        print()
    print()

