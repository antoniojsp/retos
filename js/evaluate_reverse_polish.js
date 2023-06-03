#https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/962173230/

/**
 * @param {string[]} tokens
 * @return {number}
 */
const operations = {
    "+": (x, y) => x + y,
    "-": (x, y) => x - y,
    "*": (x, y) => x * y,
    "/": (x, y) => Math.trunc(x / y),
}

var evalRPN = function(tokens) {

    var stack = []
    for (let i of tokens){
        if (!(i in operations)){
            stack.push(parseInt(i));
        }else{
            var first = stack.pop()
            var temp = operations[i](stack.pop(), first);
            stack.push(temp);
        };
    };

 return stack.pop()
};