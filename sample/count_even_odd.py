with open('even_odd.txt') as all:
    temp = all.read().split()
    result = list(map(lambda x: int(x), temp))

B = [2, 3, 4, 5, 6]
count = 0
for i in range(0, len(result)):
    if result[i]%2 != 0:
        result[i]+=1
        result[i+1] +=1
        count +=1

print(count)



