test = [-20,-3916237,-357920,-3620601,7374819,-7330761,30,6246457,-6461594,266854,-520,-470,]

def closestNumbers(arr):
    arr.sort()
    diff = {}
    smallest_diff = float("inf")
    for i in range(len(arr)-1):
        current = arr[i]
        next_index = arr[i+1]
        difference  = abs(current - next_index)

        smallest_diff = min(smallest_diff, difference)

        if difference not in diff:
            diff[abs(difference)] = [current, next_index]
        else:
            diff[abs(current - next_index)].extend([ current, next_index])

    return diff[smallest_diff]

print(closestNumbers(test))
