
//https://leetcode.com/problems/sort-by/?envType=study-plan-v2&envId=30-days-of-javascript
/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    arr.sort((a,b)=>fn(a)-fn(b));
    return arr;
};