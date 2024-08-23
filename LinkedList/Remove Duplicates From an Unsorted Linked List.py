"""
Solution 1:

Two Pass with a HashMap

Time Complexity: O()
Space complexity : O()
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        nodeCounts = defaultdict(int)
        cur = head
        while cur:
            nodeCounts[cur.val] += 1
            cur = cur.next

        dummy = ListNode(-1)
        dummy.next = head
        prev, cur = dummy, dummy.next
        while cur:
            if nodeCounts[cur.val] > 1:
                prev.next = cur.next
            else:
                prev.next = cur
                prev = cur
            cur = cur.next

        return dummy.next
