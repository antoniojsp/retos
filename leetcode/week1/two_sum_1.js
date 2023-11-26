function twoSum(nums, target){
    seen =  {}

    for(let i = 0; i < nums.length; i++){
        needs = target - nums[i]
        if(needs in seen){
            return [i, seen[needs]]
        };
        seen[nums[i]] = i
    };
};

console.log(twoSum(nums = [2,7,11,15], target = 9))