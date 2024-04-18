# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        while True:
            if not fast.next:
                break
            slow = slow.next
            if not fast.next.next:
                break
            fast = fast.next.next

        return slow