#https://leetcode.com/problems/check-if-it-is-a-straight-line/description/
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """
        If all the slopes of every single pair of points are the same then we can assume
        they are in the same line
        """
        slope = None
        for i in range(0, len(coordinates ) -1):
            """

            """
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[i+1]
            i+=1

            if not slope:
                '''
                calculate the timers slope to start the comparisons from it. 
                '''
                if x1 == x2:
                    slope = float("inf")
                else:
                    slope = (y1-y2)/(x1-x2)
            else:
                """
                After the timers slope is calculate, we calculate all the other slopes and compare with the timers one
                If any single pair of points have a different slope, then wer return False
                """
                curr_slope = float("inf") if x1 == x2 else (y1-y2)/(x1-x2)
                if slope != curr_slope:
                    return False

        return True


