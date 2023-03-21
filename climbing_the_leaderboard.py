# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true#!
# 7
# 100 100 50 40 40 20 10
# 4
# 5 25 50 120
ranking = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]


def binary_search(arr: list, val):
    start = 0
    middle = len(arr) // 2
    end = len(arr) - 1
    while True:
        if arr[middle] == val:
            return middle
        if arr[middle] < val:
            end = middle - 1
            middle = (start + end) // 2
        if arr[middle] > val:
            start = middle + 1
            middle = (start + end) // 2

def climbingLeaderboard(ranked, player):
    result = []
    for score in player:
        temp = ranked + [score]
        rank = sorted(set(temp), reverse=True)
        result.append(binary_search(rank, score)+1)

    return result

print(climbingLeaderboard(ranking, player))
