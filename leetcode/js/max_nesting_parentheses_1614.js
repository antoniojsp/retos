#https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/?envType=daily-question&envId=2024-04-04

/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function(s) {

    var stack = [];
    var count = 0;
    for (i of s){
        if(i == "("){
            stack.push("(")
            count = Math.max(count, stack.length);
        }else if (i == ")"){
            if (stack[stack.length - 1] == "("){
                stack.pop()
            }
        }
    }
    return count;

};