#https://www.youtube.com/watch?v=riBWq1DvVb8&ab_channel=Exponent

array = [1,2,3,4]
#expected result [24, 12, 8, 6]
def multiply_array(arr:list)->int:
    #first step, multiple all
    total_multiplication = 1
    for i in arr:
        if i != 0:
            total_multiplication *= i

    return total_multiplication
def product_array(arr:list)->list:
    '''
    Works for positive, negative and when there is only one zero.
    '''
    multiple = multiply_array(arr)
    if 0 in arr:
        result = [0 if i != 0  else multiple for i in arr]
    else:
        result = [int(multiple/i) for i in arr]
    return result

array = [1,0,0,2]
# [0, 0, 0, 0]
from functools import reduce
def product_array_zeros_brute(arr:list)->list:
    #brute force
    mul = lambda x, y: x*y
    result = []
    for i in range(0, len(arr)):
        arr_all_but_current = arr[0:i]+ arr[i+1:len(arr)]
        result.append(reduce(mul, arr_all_but_current))

    return result

def product_array_zeros(arr:list)->list:

    left = arr.copy()
    for i in range(1, len(left)):
        left[i] = left[i-1]*left[i]

    right = arr.copy()
    right.reverse()
    for i in range(1, len(right)):
        right[i] = right[i-1]*right[i]
    right.reverse()

    result = []
    for i in range(len(arr)):
        if i == 0:
            result.append(1*right[i+1])

        elif i == len(arr)-1:
            result.append(1*left[i-1])
        else:
            result.append(left[i-1]*right[i+1])

    return result


array = [0,1,1,2]
print(product_array_zeros(array))


