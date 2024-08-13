"""
Solution 1:

Merge Sort

Be careful about get mid function

Time Complexity: O(nlogn)
Space complexity : O(n)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode(-1)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2

        return dummy.next

    def getMid(self, head):
        if not head:
            return head

        slow = head
        fast = head
        while fast and fast.next:
            if not fast.next.next:
                break
            slow = slow.next
            fast = fast.next.next

        res = slow.next
        slow.next = None

        return res
