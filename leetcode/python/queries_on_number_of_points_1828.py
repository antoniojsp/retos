#https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/description/
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for x1, y1, r in queries:
            '''
            (x1,y1) acts like the center of the circle of a radio r
            '''
            count = 0
            for x2, y2 in points:
                """
                We calculate the distance from the center of the circle to
                a specific point. If it's equal or less than the radio, then we can
                claim that the point is inside the circle
                We use the pythogarean formula to find the distance:

                        sqrt( (x1-x2)**2 + (y1-y2)**2 ) 
                """
                distance = math.sqrt((x 1 -x2 )* *2 + (y 1 -y2 )* *2)
                if distance <= r:
                    count += 1
            answer.append(count)

        return answer
