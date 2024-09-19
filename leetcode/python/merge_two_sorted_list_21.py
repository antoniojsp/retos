# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        result = ListNode(-1)
        res = result
        temp1 = list1
        temp2 = list2

        while temp1 and temp2:
            if temp1.value <= temp2.value:
                min_val = temp1.value
                temp1 = temp1.next
            else:
                min_val = temp2.value
                temp2 = temp2.next

            result.next = ListNode(min_val)
            result = result.next

        if temp1:
            result.next = temp1
        if temp2:
            result.next = temp2

        return res.next

