//https://leetcode.com/problems/remove-element/description/

/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {

    var i = 0;
    while (i<nums.length){

        if(nums[i] == val){
            temp = nums.pop()
            if (nums.length == i){
                return nums.length
            };
            nums[i] = temp;

        }else{
            i += 1
        };

    }
    return nums.length;

};