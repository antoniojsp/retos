def kaprekarNumbers(p, q):
    # Write your code here
    for i in range(p, q+1):
        number = str(i)
        temp = str(i**2)
        # print(temp)
        length = len(number)
        # total len -
        left = str(temp[:len(temp)-length])
        right = str(temp[len(temp)-length:])

        print(left, right)







print(kaprekarNumbers(1,100))