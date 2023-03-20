lista = [23, 1, 45,33,10,222,254,2]

# [1,2,3,5,5,6,7]  lista[3] += lista[1]
# [4,2,3,5,5,6,7]   lista[0] = lista



# normal way
# lista[0], lista [3] = lista[3], lista[0]
# print(lista)

# without temp

def abs_substraction(a, b):
    return abs(a - b)

def swap_without_temp(arr, a, b):
    arr[b] = arr[a] + arr[b]
    arr[a] = abs_substraction(arr[a],arr[b])
    arr[b] = abs_substraction(arr[b], arr[a])

    return arr

print(swap_without_temp(lista,5,6))
