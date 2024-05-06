p, d, m, s = 20, 3 , 6, 70

'''
p is initial price
for each new item, the price drop in d
when price == m, then price is set up to m
s is the budget
'''


def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    spent = 0
    count = 0
    while True:
        spent += p
        count += 1
        p -= d
        if p < m:
            p = m

        if spent + p > s:
            break

    return count

print(howManyGames(p, d, m, s))