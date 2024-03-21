/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun searchBST(root: TreeNode?, value: Int): TreeNode? {
        var current:TreeNode? = root;
        var result_pointer:TreeNode? = null;
        while(current!= null){
            var current_value:Int = current.`val`;
            if (current_value == value){
                result_pointer = current;
                break;
            }else if(current_value < value){
                current  = current.right;
            }else{
                current = current.left;
            }
        }
        return result_pointer;
    }
}