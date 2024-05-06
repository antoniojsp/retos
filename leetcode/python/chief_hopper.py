from math import ceil

# arr = [4,4,4]
test = [3,4,3,2,4]

def chiefHopper(arr:list)->int:
    minimum = 0
    for height in reversed(arr):
        minimum = ceil((height+minimum)/2)
    return minimum

