# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return f"{self.name} {self.score}"
    def comparator(a, b):
        # print(a, b)
        if a.score > b.score:
            # print("a.score > b.score")
            return -1
        elif a.score < b.score:
            # print("a.score < b.score")
            return 1
        elif a.name > b.name:
            # print("a.name > b.name=1")
            return 1
        else:
            # print(0)
            return -1
    
n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)