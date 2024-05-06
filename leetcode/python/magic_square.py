a = [[1,2,3],[4,5,6],[6,7,8]]

def print_matrix(arr:list):
    for i in arr:
        print(i, sep="\n")
    print()

def rotate_matrix(arr:list, times:int)->list:
    rotated_matrix  = arr

    for i in range(0, times):
        rotated = list(zip(*rotated_matrix))[::-1]
        rotated_matrix = rotated

    return rotated_matrix

def invert_matrix(arr:list)->list:
    inverted_matrix = arr

    for i in inverted_matrix:
        i.reverse()

    return inverted_matrix

def generate_magic_squares(arr:list):
    a = arr
    for i in range(4):
        a = rotate_matrix(a, 1)
        print_matrix(a)

    rotated = invert_matrix(a)

    b  = arr
    for i in range(4):
        b = rotate_matrix(b, 1)
        print_matrix(b)


generate_magic_squares(a)