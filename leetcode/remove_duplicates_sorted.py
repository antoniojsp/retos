'''
Change array in situ and return the number of unique elements

'''
#from 4 to 1


def remove_duplicate(arr:list)->int:

    i = 0
    j = 1

    while j < len(arr):
        if arr[i] != arr[j]:
            i+=1
            arr[i] = arr[j]
        j+=1

    return i + 1

test = [0,0,1,1,1,2,2,3,3,4]

print(remove_duplicate(test))
