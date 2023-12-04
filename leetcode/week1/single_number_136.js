/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    var fun = (acc, current) => acc ^ current
    var result = nums.reduce(fun , 0)
  
    return result
};