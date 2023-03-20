from itertools import combinations

# n, a, b = 3, 1,2


# 2^n -> 2 elements, 4 combinations
# 1 1 = 2
# 1 2 = 3
# 2 1 = 3
# 2 2 = 4

n, a, b = 958, 5, 7

# 2^ (n-1) = 8 -> 3 elements 8 combinations

# 10 10 10 = 30
# 10 10 100 = 120
# 10 100 100 = 210
# 100 100 100 = 300


def stones(n, a, b):
     result = []
     for i in range(n):
          result.append((a * i) + (b * (n - i - 1)))

     return sorted(list(result))

print(stones(n, a, b))



