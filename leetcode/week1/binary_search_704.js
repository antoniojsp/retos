/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    
    var start = 0
    var end = nums.length
    while(start <= end){
        var mid  = Math.floor((start + end)/2);
        console.log(start, mid, end)
        if (nums[mid] == target){
            return mid;
        }
        if(nums[mid] > target){
            end = mid-1
        }else{
            start = mid+1
        }
    }

    return -1;
};

