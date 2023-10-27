

def digit_by_digit(n:int)->list:
    result = []
    while 0 < n:
        temp = n%10
        n//= 10
        result.append(temp)
    result.reverse()
    return result

def list_to_int(arr:list)->int:

    arr.reverse()
    result = 0
    for i,j in enumerate(arr):
        result += j*10**i

    return result


def kaprekarNumbers(p, q):
    # Write your code here
    result = []

    for i in range(p, q+1):
        squared = i**2
        number = str(i)
        n = digit_by_digit(squared)
        left = n[:len(n)-len(number)]
        right = n[len(n)-len(number):]

        if i == list_to_int(left)+list_to_int(right):
            result.append(i)

    if result:
        # for i in result:
        #     print(i, end=" ")
        print(*result)
    else:
        print("INVALID RANGE")


    #     number = str(i)
    #     squared = str(i**2)
    #     temp_l = str(squared[:len(squared)-len(number)])
    #     left = int(temp_l) if temp_l else 0
    #
    #     temp_r = str(squared[len(squared)-len(number):])
    #     right = int(temp_r) if temp_r else 0
    #
    #     if left + right == i:
    #         result.append(i)
    #
    # if result:
    #     for i in result:
    #         print(i, end=" ")
    # else:
    #     print("INVALID RANGE")

kaprekarNumbers(1,100)