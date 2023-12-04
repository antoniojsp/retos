//https://leetcode.com/problems/majority-element/
var majorityElement = function(nums){
    nums.sort();
    console.log(nums)
    return nums[nums.length/2]
    // var seen = {}
    // for(let i of nums){
    //     if(!(i in seen)){
    //          seen[i]=0
    //     }
    //     seen[i]+=1
    //     if(seen[i]>nums.length/2){
    //         return i
    //     }
    // };
};