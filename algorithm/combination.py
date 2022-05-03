
a = [1,2,3,3]
temp = []
for i in range(0, len(a)):
    for j in range(i, len(a)+1):
        if i == j:
            continue
        else:
            temp.append(a[i:j])


print(temp)

