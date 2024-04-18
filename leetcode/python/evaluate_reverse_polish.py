from math import floor

map_operators = {
"+":lambda x, y:x + y,
"-": lambda x, y: x - y,
"/": lambda x, y: int(x / y),
"*": lambda x, y: x * y,
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in map_operators:
                stack.append(int(i))
            else:
                temp = stack.pop()
                temp = map_operators[i](stack.pop(), temp)
                stack.append(temp)

        return stack.pop()