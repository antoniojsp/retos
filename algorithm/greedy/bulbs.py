

def inverse(arr:list)->list:
    return [int(not i) for i in arr]
def cost_bulbs(arr):
    both = {"a":arr, "b":inverse(arr)}

    i = 0
    cost = 0
    current = "a"
    while i < len(arr):
        if both[current][i] == 0:
            cost += 1
            current = "a" if current == "b" else "b"
        i += 1

    return cost


print(cost_bulbs([1,0,0,0]))


def bulbs(a):
    cost = 0
    for b in a:
        if cost%2==0:
            b = b
        else:
            b = not b

        if b % 2 == 1:
            continue
        else:
            cost +=1

    return cost

print(bulbs([1,0,1,0]))
