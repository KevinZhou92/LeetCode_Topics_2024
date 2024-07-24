"""
Solution 1:

Priority Queue

It's essentially merge k sorted list, here we don't care about the order between previous k
elements, we just care about what is Kth element. 

PQ stores the smallest element for each row, which guarantes every selection we are selecting
the minimum value out of all rows.

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

"""
Solution 1:

Binary Search

Time Complexity: O(Nlog1)
Space complexity : O()
"""
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        start, end = 0, 1
        while start < end:
            mid = start + (end - start) / 2
            cnt, res = self.findCount(arr, mid)
            if cnt == k:
                return res
            elif cnt > k:
                end = mid
            else:
                start = mid
        
        return []
    
    def findCount(self, arr, target):
        curMax = 0
        numerator, denominator = 0, 0
        r = 1
        cnt = 0
        for l in range(len(arr) - 1):
            while r < len(arr) and arr[l] >= target * arr[r]:
                r += 1
                        
            cnt += (len(arr) - r)

            if r == len(arr):
                break

            if arr[l] / arr[r] > curMax:
                numerator = l
                denominator = r
                curMax = arr[l] / arr[r]
        
        return cnt, [arr[numerator] , arr[denominator]]
