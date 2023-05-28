/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {

    var temp = head
    var prev = null;

    while (temp){
        next_node = temp.next
        temp.next = prev
        prev = temp
        temp = next_node
    };

    return prev
};