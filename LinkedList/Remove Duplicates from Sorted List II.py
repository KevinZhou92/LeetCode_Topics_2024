"""
Solution 1:

Sentinel + Predecessor

Time Complexity: O(N)
Space complexity : O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while head:
            if head and head.next and head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev.next = head
                prev = head
            head = head.next

        return dummy.next
