/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {

    var start = 0;
    var end = nums.length-1;

    while (start <= end){

        const mid = Math.floor( (start + end)/2 );

        if (nums[mid] == target){
            return mid;
        }

        if (nums[mid] > target){
            end = mid - 1;
        }else{
            start = mid + 1;
        }
    };

    return -1;

};