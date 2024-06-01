#https://www.youtube.com/watch?v=riBWq1DvVb8&ab_channel=Exponent

array = [1,2,3,4]

from functools import reduce
def product_array_zeros_brute(arr:list)->list:
    #brute force 0(n^2)
    mul = lambda x, y: x*y
    result = []
    for i in range(0, len(arr)):
        arr_all_but_current = arr[0:i]+ arr[i+1:len(arr)]
        result.append(reduce(mul, arr_all_but_current))
    return result

def product_array_zeros(arr:list)->list:
    '''
    O(n)
    '''

    left = arr.copy()
    for i in range(1, len(left)):
        left[i] = left[i-1]*left[i]

    right = arr.copy()
    right.reverse()
    for i in range(1, len(right)):
        right[i] = right[i-1]*right[i]
    right.reverse()

    result = [right[1]]
    for i in range(1, len(arr)-1):
        result.append(left[i-1]*right[i+1])
    result.append(left[-2])

    return result


def multiply(arr:list)->int:
    result = 1
    for i in arr:
        if i != 0:
            result *=i

    return result

def locate_zeros(arr:list)->int:
    result = []
    for i, j in enumerate(arr):
        if j == 0:
            return i

    return -1

print(locate_zeros([1,2,3,4,5,0]))


