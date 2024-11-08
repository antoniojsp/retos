# https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75
from typing import List


class Solution:

    @staticmethod
    def check_signs(a, b):
        first = a > 0
        second = b > 0
        return first == second
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        s = []

        while asteroids:
            if not s:
                s.append(asteroids.pop())
            else:
                temp_stack = s.pop()
                temp_asteroid = asteroids.pop()

                if not self.check_signs(temp_stack, temp_asteroid):

                    if temp_stack + temp_asteroid == 0:
                        continue
                    value = temp_stack if abs(temp_stack)>abs(temp_asteroid) else temp_asteroid
                    s.append(value)
                else:
                    print("thj")
                    s.append(temp_asteroid)
                    s.append(temp_stack)

        return s


# def check_signs(a, b):
#     timers = a>0
#     second = b>0
#     return timers == second
#
# print(check_signs(1, 5))





print(Solution().asteroidCollision(asteroids = [-2,-1,1,2]))

[-2,-1,1,2]
[]

[-2,-1,1]
[2]

[-2,-1]
[1,2]

