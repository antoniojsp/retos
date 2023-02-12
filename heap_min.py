# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/qheap1/problem?isFullScreen=true
def heapify(arr: list):
    for i, j in enumerate(arr):
        current = i
        while True:
            parent = (current - 1) // 2
            if parent < 0:
                break
            elif arr[parent] > arr[current]:
                arr[parent], arr[current] = arr[current], arr[parent]
                current = parent
            else:
                break
    return arr


def add(arr: list, val: int) -> list:
    arr.append(val)
    current = len(arr) - 1
    while True:
        parent = (current - 1) // 2
        if current == 0:
            break
        elif arr[parent] > arr[current]:
            arr[current], arr[parent] = arr[parent], arr[current]
            current = parent
        else:
            break

    return arr


def delete(arr: list, val: int):
    '''
    Assuming that any value given to search is present in the heap
    '''

    if val not in arr:
        return

    parent = arr.index(val)
    arr[parent] = arr[-1]
    arr.pop()

    while parent < len(arr):

        left = parent * 2 + 1
        right = parent * 2 + 2

        if left > len(arr) - 1:
            break

        if right > len(arr) - 1:
            if arr[parent] > arr[left]:
                arr[parent], arr[left] = arr[left], arr[parent]
            break

        l_val = arr[left]
        r_val = arr[right]

        minimum = left if l_val < r_val else right

        if arr[parent] > arr[minimum]:
            arr[parent], arr[minimum] = arr[minimum], arr[parent]
            parent = minimum
        else:
            break

    return arr


queries = input()
result = []

for i in range(int(queries)):
    val = input().split()
    if val[0] == "1":
        result = add(result, int(val[1]))

    elif val[0] == "2":
        result = delete(result, int(val[1]))

    else:
        print(result[0])


