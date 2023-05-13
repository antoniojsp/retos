# https://leetcode.com/problems/3sum/


def dict_values(arr:list)->dict:
    result =  {}
    for i, j in enumerate(arr):
        if j not in result:
            result[j] = set()
        result[j].add(i)

    return result


nums = [-1,0,1,2,-1,-4]
# nums = [0,0,0]

#di = {0:{0,1,2}}

def threesum(arr:list)->list:
    arr.sort()
    print(arr)
    data = dict_values(arr)
    print(data)
    result = []
    prev = None
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        target = -arr[i]

        for j in range(i+1, len(arr)):
            if prev is None or prev != arr[j]:
                # prev = arr[j]
                remainder = -(arr[i]+arr[j])
                # print(arr[j+1:len(arr)], remainder)

                temp = dict_values(arr[j+1:len(arr)])

                if remainder in temp:
                    # if len(data[remainder]-l)>0:
                    temp = [arr[i], arr[j],remainder]
                    # temp.sort()
                    if temp not in result:
                        result.append(temp)


                # if remainder in data:
                #     l = {i, j}

                    # if len(data[remainder]-l)>0:
                    #     temp = [arr[i], arr[j],remainder]
                    #     temp.sort()
                    #     if temp not in result:
                    #         result.append(temp)

    return result

print(threesum(nums))