var isValid = function(s) {
    let stack = [];
    for (let idx = 0; idx < s.length; idx++) {
        if (s[idx] == '{') {
            stack.push('}');
        } else if (s[idx] == '[') {
            stack.push(']');
        } else if (s[idx] == '(') {
            stack.push(')');
        }
        else if (stack.pop() !== s[idx]) {
            return false;
        }
    }
    return !stack.length;
};


const assert = require('assert');

// Test 1: Testing a simple valid case
assert.strictEqual(isValid("()"), true, "Expected true for input '()'");

// Test 2: Testing nested valid parentheses
assert.strictEqual(isValid("{[()]}"), true, "Expected true for input '{[()]}'");

// Test 3: Testing an invalid case with mismatched parentheses
assert.strictEqual(isValid("{[(])}"), false, "Expected false for input '{[(])}'");

// Test 4: Testing an edge case with empty string
assert.strictEqual(isValid(""), true, "Expected true for an empty string");

// Test 5: Testing an invalid case where more opening parentheses than closing
assert.strictEqual(isValid("({[)"), false, "Expected false for input '({[)'");

console.log("All tests passed!");