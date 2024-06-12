"""
Solution 1:

1. Count the length of the list
2. Connect the list's head and tail
3. Find out the node to break the circle to get the new list

Note that k might be greater than the length of the list

Time Complexity: O(n)
Space complexity : O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
            
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        length = 1
        # Count the length of the list
        while cur.next:
            cur = cur.next
            length += 1
        
        # Connect tail with head to make a circle
        cur.next = head

        k = length - k % length
        for _ in range(k):
            dummy = dummy.next
        
        res = dummy.next
        dummy.next = None

        return res
        