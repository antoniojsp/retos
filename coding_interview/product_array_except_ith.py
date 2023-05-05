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
    #case one zero
    multiple = multiply_array(arr)
    if 0 in arr:
        result = [0 if i != 0  else multiple for i in arr]
    else:
        result = [int(multiple/i) for i in arr]
    return result


print(product_array([1,2,0,0]))

#what if array [1,2,0,4]