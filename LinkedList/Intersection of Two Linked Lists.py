"""
Solution 1:

Loop over both lists to get the length of both lists and capture the diff in length
Move the head pointer of the longer list diff steps so both pointers are same distance away from the intersection
Move both pointers until they are the same node

Time Complexity: O(n)
Space complexity : O(n)
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        p1, p2 = headA, headB
        len1, len2 = 1, 1
        while p1:
            p1 = p1.next
            len1 += 1

        while p2:
            p2 = p2.next
            len2 += 1

        # Make len1 always represent the shorter list
        if len1 > len2:
            len1, len2 = len2, len1
            headA, headB = headB, headA
        
        for _ in range(len2 - len1):
            headB = headB.next
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA

"""
Solution 2:

Assume A is length M, B is length N, we will have two pointers to move along each list and point to the 
head of other list if we finished going over one list.

In this case, if two list intersects, at end of the day, the two pointer will meet at the intersection
point since they just walk the same distance and the intersection point can only be when both pointers first meet.


Time Complexity: O(n)
Space complexity : O(n)
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        return pA
        
