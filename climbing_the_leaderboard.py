# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true#!
# 7
# 100 100 50 40 40 20 10
# 4
# 5 25 50 120
ranking = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]

def climbingLeaderboard(ranked, player):

    for i in player:
        temp = ranked + [i]
        temp.sort()
        new = set(temp)
        sorted_list = list(new)[::-1]
        print(sorted_list)

climbingLeaderboard(ranking, player)