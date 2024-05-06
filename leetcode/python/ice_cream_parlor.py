
# def icecreamParlor(m, arr):
#     for i in range(len(arr)):
#         j = i+1
#         while j < len(arr):
#             if arr[i] + arr[j] == m:
#                 return [i+1, j+1]
#             j+=1
#
#     return []

# print(icecreamParlor(k, a))

a = [2, 2, 4, 3]

k = 4
# a = [1, 4, 5, 3, 2]
def iceCreamParlor(m, arr):
    dictio = {}
    for i, j in enumerate(a, 1):
        need = k - j
        if need in dictio:
            return [dictio[need], i]
        else:
            dictio[j] = i







