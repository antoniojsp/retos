class Solution:
    def sumOfMultiples(self, n: int) -> int:
        candidates: List[int] = []
        for i in range(n+1):
            if i%3 == 0 or i%5 == 0 or i%7 == 0:
                candidates.append(i)
        return sum(candidates)