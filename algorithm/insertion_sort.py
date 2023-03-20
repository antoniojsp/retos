arr = [4,3,2,1]

for i in range(1, len(arr)):
    current = i

    while True:
        if current < 0:
            break
        elif arr[current] < arr[current-1]:
            arr[current],  arr[current- 1] = arr[current-1], arr[current]
            current -= 1
        else:
            break

print(arr)
