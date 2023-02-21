n = 132
prev = 1
for i in range(0,64):

    if 2**i > n:
        print(prev)
        break

    prev = 2**1