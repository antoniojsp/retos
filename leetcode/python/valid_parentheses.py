# https://leetcode.com/problems/valid-parentheses/

def isValid(s: str) -> bool:
    result = []
    mapa = {"{": "}", "(": ")", "[": "]"}
    for i in s:
        if i in ["[", "{", "("]:
            result.append(i)
        else:
            if not result:
                return False
            temp = result.pop()
            if i != mapa[temp]:
                return False

    return len(result) == 0


print(isValid("}"))
