"""
Solution 1:

Iterative Solution

Time Complexity: O(n)
Space complexity : O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        tail = None
        while head:
            nextHead = head.next
            head.next = tail
            tail = head
            head = nextHead

        return tail
