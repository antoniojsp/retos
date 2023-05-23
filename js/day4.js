// https://datayi.cn/w/noqbNOv9

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    result = []
    for(let i = 0; i< arr.length; i++){
        result.push(fn(arr[i], i));
    };

    return result
};