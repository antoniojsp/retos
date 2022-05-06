#https://www.hackerrank.com/challenges/three-month-preparation-kit-separate-the-numbers/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-four
from math import floor
s = "1234"

def separateNumbers(s):

    lenght = len(s)
    for i in range(0, floor(len(s)/2)):
        current = s[:i]
        for j in range(1, floor(len(s)/2)):
            print(current)
            print((s[i:j]))

        print(current)


separateNumbers(s)