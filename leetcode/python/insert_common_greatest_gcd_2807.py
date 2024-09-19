#https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/
from math import gcd

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    @staticmethod
    def gcd(a ,b )->int:
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a


    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current.next:
            gcd_val = self.gcd(current.value, current.next.value)
            new_node = ListNode(gcd_val)
            next = current.next
            current.next = new_node
            current.next.next = next
            current = current.next.next

        return head
