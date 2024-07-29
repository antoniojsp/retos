arr = [1,-2,3,-4]


def count_positive(arr):
    result = 0
    for i in arr:
        if i >= 0:
            result+=1

    return result

print(count_positive(arr))