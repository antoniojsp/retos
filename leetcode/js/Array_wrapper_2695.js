/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.nums = nums;
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    result = 0
    for(let i of this.nums){
        result+=i
    }
    return result;
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    return '[' + this.nums.toString() + ']';
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */