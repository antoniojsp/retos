
https://leetcode.com/problems/xor-operation-in-an-array/description/v

/**
 * @param {number} n
 * @param {number} start
 * @return {number}
 */
var xorOperation = function(n, start) {

    var arr = [];
    for(let i = 0; i<n; i++){
        arr.push(start+2*i);
    }
    var answer = arr.reduce((accumulator, currentValue) => accumulator ^ currentValue)

    return answer;
};