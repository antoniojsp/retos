#https://www.hackerrank.com/challenges/three-month-preparation-kit-stockmax/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-nine
"""
detect arrays that are in ascending order
i.e
[1,2,3] good
[2,7,10] good
[1,3,1,6] good
[1,3,2,1] good
[5,2,1] bad
"""


def stockmax(prices):
    max_price = prices[-1]
    suma = 0
    for i in reversed(prices):
        if max_price > i:
            suma += max_price - i
        else:
            max_price = i

    return suma

a = [1,3,1,2]
print(stockmax(a))







