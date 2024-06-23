test = [1,0,1,0,1]

def bulbs(arr:list)->int:

    is_original = True
    cost = 0
    for i in arr:
        if i == 0 and is_original or i == 1 and not is_original:
            cost+=1
            is_original = not is_original

    return cost

print(bulbs(test))
