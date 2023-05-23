https://datayi.cn/w/a9a5VZr9

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    result = []
    for (let i = 0; i < arr.length; i++){
        if (fn(arr[i], i)){
            result.push(arr[i]);
        };
    };
    return result;
};