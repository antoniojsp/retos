class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0

        for type1, color, name in items:
            item = {"type": type1, "color": color, "name": name}
            if item[ruleKey] == ruleValue:
                count += 1

        return count
