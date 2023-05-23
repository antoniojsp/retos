https://leetcode.com/problems/array-reduce-transformation/submissions/?utm_campaign=PostD6&utm_medium=Post&utm_source=Post&gio_link_id=nPN45jD9

/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init){

    for (let i = 0; i < nums.length; i++){
      init = fn(init, nums[i]);
    };
    return init;
  };