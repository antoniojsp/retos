test = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]

unique = []
for i in test:
    unique.append(set(i))

inter1 = unique[0].intersection(unique[1])
inter2 = unique[1].intersection(unique[2])
inter3 = unique[0].intersection(unique[2])
print(inter1, inter2, inter3)