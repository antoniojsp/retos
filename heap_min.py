
def heapify(arr:list):
    for i, j in enumerate(arr):
        current = i
        while True:
            parent = (current-1)//2
            if current == 0:
                break
            if  arr[parent] > arr[current]:
                arr[parent], arr[current] = arr[current], arr[parent]
                current = parent
            else:
                break
    return arr

def add(arr: list, val:int)->list:
    arr.append(val)
    current = len(arr)-1
    while current != 0:
        parent = (current-1)//2

        if arr[parent] > arr[current]:
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

        left = parent*2+1
        right = parent*2+2

        if left > len(arr)-1:
            break

        if right > len(arr)-1:
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







# result = [23,1,2,56,3,25,13,5,89,7,4,134,4]
# result = heapify(result)
# print(result)
new = []
result = [23,1,2,56,3,25,13,5,89,7,4,134,4]

for i in result:
    add(new, i)

print(new)
# delete(new, 2)
# print(new)








