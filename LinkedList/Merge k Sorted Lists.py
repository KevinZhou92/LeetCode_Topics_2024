"""
Solution 1:
PriorityQueue + Dummy Head

The tricky thing here is to understand how to write a custom comparator for PQ


Time Complexity: O(NlogK)
Space complexity : O(n) for create a new linked list, O(k) for priority queue
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class HeapNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        # Define comparison based on ListNode's value
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        dummy = ListNode(-1)
        tail = dummy
        
        pq = []
        for head in lists:
            if not head:
                continue
            heapq.heappush(pq, HeapNode(head))
        
        while pq:
            heap_node = heappop(pq)
            node = heap_node.node
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(pq, HeapNode(node.next))
            
        return dummy.next
        
"""
Solution 2:

Bottom-up Merge Sort


Time Complexity: O(NlogK), k is the # of lists
Space complexity : O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        count = len(lists)
        interval = 1
        while interval < count:
            for i in range(0, count - interval, interval * 2):
                lists[i] = self.merge_two_lists(lists[i], lists[i + interval])
            interval *= 2
        
        return lists[0]

    def merge_two_lists(self, l1, l2):
        dummy = ListNode(-1)
        head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        while l1:
            head.next = l1
            l1 = l1.next
            head = head.next
        
        while l2:
            head.next = l2
            l2 = l2.next
            head = head.next
        
        return dummy.next