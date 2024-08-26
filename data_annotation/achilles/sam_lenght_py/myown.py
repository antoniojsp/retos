test = [(11, 22, 33), (44, 55, 66)]

def same_length(arr:list)-> bool:
    lengths = [len(i) for i in arr]
    unique = set(lengths)
    return len(unique) == 1

print(same_length(test))