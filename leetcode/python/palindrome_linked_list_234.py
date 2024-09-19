# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        visited = []
        temp = head
        while temp:
            visited.append(temp.value)
            temp = temp.next

        return visited == list(reversed(visited))


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return True

        slow = head
        fast = head

        # find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse one of the lists
        current = slow
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        slow = prev
        while slow and head:
            if slow.val != head.value:
                return False
            slow = slow.next
            head = head.next

        return True







