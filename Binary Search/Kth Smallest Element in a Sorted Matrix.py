"""
Solution 1:

PriorityQueue

Time Complexity: O(NLogK)
Space complexity : O(1)
"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return -1

        pq = []
        for r in range(len(matrix)):
            heapq.heappush(pq, [matrix[r][0], r, 0])

        for _ in range(k - 1):
            cur, r, c = heapq.heappop(pq)
            if c + 1 < len(matrix[0]):
                heapq.heappush(pq, [matrix[r][c + 1], r, c + 1])

        res, _, _ = heapq.heappop(pq)

        return res


"""
Solution 2:

Binary Search

Time Complexity: O(NlogC)
Space complexity : O(1)
"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return -1

        r = len(matrix)
        c = len(matrix[0])
        start, end = matrix[0][0], matrix[r - 1][c - 1]
        while start + 1 < end:
            mid = start + (end - start) // 2
            cnt, res = self.findSmaller(matrix, mid)
            if cnt >= k:
                end = mid
            else:
                start = mid

        cnt, res = self.findSmaller(matrix, start)
        if cnt >= k:
            return res

        return end

    def findSmaller(self, matrix, target):
        cnt = 0
        res = 0
        n = len(matrix)
        r, c = n - 1, 0
        while r >= 0 and c < n:
            if matrix[r][c] > target:
                r -= 1
            else:
                res = matrix[r][c]
                cnt += r + 1
                c += 1

        return cnt, res
