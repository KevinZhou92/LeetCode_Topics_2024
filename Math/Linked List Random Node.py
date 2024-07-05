"""
Solution 1:

Use extra space to store the list
Generate a random index and pick the element
Can't work for an input with unknown length

Time Complexity: O(N)
Space complexity : O(N)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.elements = []
        while head:
            tmp = head.next
            self.elements.append(head)
            head.next = None
            head = tmp

    def getRandom(self) -> int:
        rand = random.randint(0, len(self.elements) - 1)
        return self.elements[rand].val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

"""
Solution 1:

Reservoir Sampling

Time Complexity: O(N)
Space complexity : O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        count = 1
        cur = self.head
        # We can set res to 0 since at first iteration it will be set to value of the first element
        # since the probability is 1/i which is 1 at first iteration
        res = 0
        while cur:
            rand = random.randint(1, count)
            if rand == count:
                res = cur.val
            cur = cur.next
            count += 1
            
        return res
        