groupSizes = [3,3,3,3,3,1,3]

temp = {}
for i, j in enumerate(groupSizes):
    if j not in temp:
        temp[j] = []
    temp[j].append(i)


