"""
Solution 1:

Be careful about how the linked list is stored

Time Complexity: O(max(m, n))
Space complexity : O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        res = []
        carry = 0
        head = ListNode(-1)
        tail = head
        while l1 and l2:
            l1Val = l1.val
            l2Val = l2.val
            curSum = l1Val + l2Val + carry
            curNode = ListNode(curSum % 10)
            tail.next = curNode
            tail = tail.next
            carry = curSum // 10
            l1 = l1.next
            l2 = l2.next

        while l1:
            l1Val = l1.val
            curSum = l1Val + carry
            curNode = ListNode(curSum % 10)
            tail.next = curNode
            tail = tail.next
            carry = curSum // 10
            l1 = l1.next

        while l2:
            l2Val = l2.val
            curSum = l2Val + carry
            curNode = ListNode(curSum % 10)
            tail.next = curNode
            tail = tail.next
            carry = curSum // 10
            l2 = l2.next

        if carry:
            curNode = ListNode(carry % 10)
            tail.next = curNode
            tail = tail.next

        return head.next
