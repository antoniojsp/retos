

# https://leetcode.com/problems/remove-linked-list-elements/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        answer = ListNode(-1)
        dummy = answer
        current = head
        while current:
            if current.value != val:
                new_node = ListNode(current.value)
                dummy.next = new_node
                dummy = dummy.next
            current = current.next

        return answer.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        answer = ListNode(-1)
        answer.next = head
        current = answer

        while current.next:
            if current.next.value == val:
                current.next = current.next.next
            else:
                current = current.next

        return answer.next



