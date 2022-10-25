a = [1, 2, 5, 3, 2, 5, 6, 7, 8, 8, 0, 2, 1,1, 7]


def counting_sort(arr) -> list:
    counting_arr = [0]*(max(a)+1)
    for i in arr:
        counting_arr[i] += 1
    print(counting_arr)
    for i in range(1, len(counting_arr)):
        counting_arr[i] = counting_arr[i] + counting_arr[i-1]

    output = [None]*len(a)

    for i in arr:
        counting_arr[i] -= 1
        output[counting_arr[i]] = i
        print(counting_arr)
    return output

print(a)
print(counting_sort(a))

#
# def list_to_array(arr) -> str:
#     result = ""
#     for i in arr:
#         result += str(i) + " "
#
#     return result[:-1]  # clean last " " space in the string
#
#
# # def counting_sort(arr)->list:
# #     max_key_value = int(max(arr)[0])+1
# #     dict_result = {i: [] for i in range(max_key_value)}
#
# #     for index, value in enumerate(arr):
# #         current_element = int(arr[index][0])
# #         if index < len(arr)/2:
# #             dict_result[current_element].append("-")
# #         else:
# #             dict_result[current_element].append(arr[index][1])
# #     result = ""
#
# #     for i in dict_result.values():
# #         if i:
# #             temp = list_to_array(i)
# #             result += temp + " "
#
# #     return result
#
#
# def counting_sort(arr) -> list:
#     counting_arr = [0] * (int(max(arr)[0]) + 1)
#     for i in arr:
#         counting_arr[int(i[0])] += 1
#     # print(counting_arr)
#     for i in range(1, len(counting_arr)):
#         counting_arr[i] = counting_arr[i] + counting_arr[i - 1]
#     print(counting_arr)
#
#     output = [[]] * len(arr)
#     # print(output)
#     for index in arr:
#         counting_arr[int(index[0])] -= 1
#         print(counting_arr)
#         print(index[1])
#         print(output[counting_arr[int(index[0])]])
#         output[counting_arr[int(index[0])]] += [index[1]]
#         print(output)
#     return output
#
#
# def add_dash(arr) -> list:
#     lenght = int(len(arr) / 2)
#     for i in range(0, lenght):
#         arr[i][1] = "-"
#     return arr
#
#
# def countSort(arr):
#     temp = add_dash(arr)
#     result = counting_sort(temp)
#     print(result)
#
#
