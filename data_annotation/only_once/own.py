arr =  [1,1,2,2,3]


def check_unique(arr:list)->int:
    seen = {}

    for i in arr:
        seen[i] = seen.get(i, 0) + 1
    print(seen)
    for i, j in seen.items():
        if j == 1:
            return i

print(check_unique(arr))