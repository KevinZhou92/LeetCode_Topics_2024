"""
Solution 1:

Reverse Second Half of list and compare.
Restore it after comparison

Time Complexity: O(N)
Space complexity : O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        # Find mid node
        firstHalfEnd = self.findFirstHalfEnd(head)
        tmp = firstHalfEnd.next
        firstHalfEnd.next = None
        secondHalfStart = self.reverseList(tmp)
        res = True
        l, r = head, secondHalfStart
        while l and r:
            if l.val != r.val:
                res = False
                break
            l = l.next
            r = r.next

        firstHalfEnd.next = self.reverseList(secondHalfStart)

        return res

    def findFirstHalfEnd(self, head):
        slow, fast = head, head
        while fast and fast.next:
            if not fast.next.next:
                break
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, head):
        prev = None
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode

        return prev
