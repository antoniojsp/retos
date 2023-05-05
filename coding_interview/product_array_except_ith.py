#https://www.youtube.com/watch?v=riBWq1DvVb8&ab_channel=Exponent

array = [1,2,3,4]
#expected result [24, 12, 8, 6]

def product_array(arr:list)->list:
    #first step, multiple all
    total_multiplication = 1
    for i in arr:
        total_multiplication *= i
    #second divide the first result with each element of the array
    return [int(total_multiplication/i) for i in arr]

print(product_array(array))