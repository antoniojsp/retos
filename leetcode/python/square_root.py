class Solution:
    def mySqrt(self, x: int) -> int:
        temp = x
        count = 0
        for i in range(1, x+1, 2):
            temp = temp - i
            if i*i == x:
                break
            if temp < 0:
                break
            count +=1

        return count

test = 200
i = 1
while i*i<test:
    i +=i

print(i)

a = Solution()

# print(a.mySqrt(225))
