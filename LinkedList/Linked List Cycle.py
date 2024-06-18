"""
Solution 1:

Two Pointer Template

Time Complexity: O(n)
Space complexity : O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # break
                return True
        
        if not fast or not fast.next:
            return False

        # slow = head
        # while slow:
        #     slow = slow.next
        #     if slow == fast:
        #         return True
        
        return False