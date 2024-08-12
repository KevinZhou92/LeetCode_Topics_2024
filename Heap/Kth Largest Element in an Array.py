"""
Solution 1:

PriorityQueue. Min Heap

Time Complexity: O(NlogK)
Space complexity : O(K)
"""


class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
