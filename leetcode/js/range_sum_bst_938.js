//https://leetcode.com/problems/range-sum-of-bst/submissions/1244476905/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var rangeSumBST = function(root, low, high) {

    Q = [root];
    var count = 0;
    while(Q.length > 0){
        var temp = Q.shift();

        if (temp.val >= low && temp.val <= high){
            count+=temp.val;
        }

        if(temp.left !== null){
            Q.push(temp.left);
        }


        if(temp.right !== null){
            Q.push(temp.right);
        }

    }

    return count;

};


