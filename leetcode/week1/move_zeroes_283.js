/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] == 0) {
      var move = i+1
      console.log(nums[i]);
      while (move < nums.length){
        if (nums[move] != 0) {
          nums[i] = nums[move];
          nums[move] = 0;
          break;
        }
        move += 1;
      };
    };
  };
  return nums;
};