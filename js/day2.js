//https://leetcode.com/problems/counter/submissions/?utm_campaign=PostD2&utm_medium=Post&utm_source=Post&gio_link_id=xogkVqBo

/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    // let temp = n
    return function() {

        return n++;
    };
};

/**
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */