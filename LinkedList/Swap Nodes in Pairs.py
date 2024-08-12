"""
Solution 1:

Recursion

Time Complexity: O(N)
Space complexity : O(N)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        remains = head.next.next
        first = head
        second = head.next
        second.next = first
        dummy.next = second
        first.next = self.swapPairs(remains)

        return dummy.next
