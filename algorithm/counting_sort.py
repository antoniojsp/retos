a = [1, 2, 5, 3, 2, 5, 6, 7, 8, 8, 0, 2, 1,1, 7]


def counting_sort(arr) -> list:
    counting_arr = [0]*(max(a)+1)
    for i in arr:
        counting_arr[i] += 1

    for i in range(1,len(counting_arr)):
        counting_arr[i] = counting_arr[i] + counting_arr[i-1]

    output = [None]*len(a)

    for i in arr:
        counting_arr[i] -= 1
        output[counting_arr[i]] = i


    return output

print(counting_sort(a))

