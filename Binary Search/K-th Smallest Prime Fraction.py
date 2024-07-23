"""
Solution 1:

Priority Queue

It's essentially merge k sorted list, here we don't care about the order between previous k
elements, we just care about what is Kth element.

Time Complexity: O(nlogn + klogn)
Space complexity : O(n)
"""


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        if not arr:
            return []

        n = len(arr)
        pq = []
        for i in range(n - 1):
            heapq.heappush(pq, (arr[i] / arr[-1], i, n - 1))

        for _ in range(k - 1):
            curMin, index1, index2 = heapq.heappop(pq)
            if index2 - 1 > index1:
                heapq.heappush(pq, (arr[index1] / arr[index2 - 1], index1, index2 - 1))

        _, index1, index2 = heapq.heappop(pq)
        return [arr[index1], arr[index2]]
