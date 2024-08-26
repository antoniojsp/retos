test = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]

def extract_first(arr:list)->list:

    return [i[0] for i in arr]

print(extract_first(test))