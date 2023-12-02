//https://leetcode.com/problems/implement-queue-using-stacks/description/
var MyQueue = function() {
    this.first = []
    this.second = []
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    //0(1)
    this.first.push(x)
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    //O(n)
    var length = this.first.length
    for(let i = 0; i < length - 1; i++){
      this.second.push(this.first.pop());
    }
    var result = this.first.pop();
  
    var length = this.second.length
    for(let i = 0; i < length ; i++){
      this.first.push(this.second.pop())
    }
  
    return result;
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    //O(1)
    return this.first[0];
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    //0(1)
    return this.first.length == 0;
};

/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */