#https://www.hackerrank.com/challenges/three-month-preparation-kit-smart-number/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-five

import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    if val*val == num:
    #perfect squares have odd factos since in other values, there is always two factors to make up the value but in squares, there is one withoug pair, the square root.
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")