"""
Solution 1:

Two Pointer

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
        if not head:
            return None

        # two pointer, one track the tail of the non-duplicate linkedlist
        # one scan throught the linked list, if p2 is the same as p1, we iterate to next since we don't want any duplicate
        p1, p2 = head, head
        while p2:
            if p1.val == p2.val:
                p2 = p2.next
                p1.next = p2
            else:
                p1.next = p2
                p1 = p1.next

        return head
