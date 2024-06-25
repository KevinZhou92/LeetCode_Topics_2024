"""
Solution 1:

Slow-fast pointer

Time Complexity: O(N)
Space complexity : O(1)
"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head

        slow, fast = dummy, dummy
        for _ in range(n):
            if not fast:
                continue
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        if slow and slow.next:
            slow.next = slow.next.next

        return dummy.next
