#https://leetcode.com/problems/path-crossing/description/
class Solution:
    def isPathCrossing(self, path: str) -> bool:

        current = [0, 0]
        visited = set([str(current)])

        for i in path:
            match i:
                case "N":
                    current[1] += 1
                case "S":
                    current[1] -= 1
                case "E":
                    current[0] += 1
                case "W":
                    current[0] -= 1
            if str(current) in visited:
                return True
            visited.add(str(current))

        return False






