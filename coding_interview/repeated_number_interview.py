#https://www.youtube.com/watch?v=clMJ8BwCGa0&ab_channel=Exponent
import math
array = [1,2,3,4,1]

def find_repeated_number(arr:list)->int:
    '''
    brute force solution to find a repeated number. We know there is only one repeated number
    o(n^2)
    '''
    for i in range(0, len(arr)):
        temp = arr[0:i] + arr[i+1:len(arr)]
        if arr[i] in temp:
            return arr[i]

    return -1

def find_array_good(arr:list)->int:

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]

    return -1

# print(find_array_good([1,2,3,4,7,10,3,12]))

def find_repeated_number_better(arr:list)->int:
    '''
    Complexity sort o(nlogn)
    nope: modify array
    '''
    if not arr or len(arr) < 2:
        return -1
    arr.sort()
    temp = None
    for i in arr:
        if temp is None or temp != i:
            temp = i
        elif temp == i:
            return i

    return -1


def find_repeated_bitarray(arr:list)->int:
    '''
    Accept zeros
    time complexity 0(n)
    space  complexity ?

    '''
    if not arr:
        return -1

    storage = None
    for i in arr:
        if storage is None:
            storage = 1<<i+1
            continue

        move = 1<<(i+1)
        suma = storage + move
        storage = storage ^ move
        if storage != suma:
            return i

    return -1


def find_repeated_mark(arr:list)->int:
    '''
    number of elements (max n+1)
    range 1 to n
    '''

    for i in range(0, len(arr)):
        current = abs(arr[i])-1

        if arr[current] < 0:
            return abs(arr[i])
        arr[current] = -arr[current]
    return -1

print(find_repeated_mark([2,6,4,3,6,5,1]))


