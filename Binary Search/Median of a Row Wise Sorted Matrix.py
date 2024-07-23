"""
Solution 1:

Binary Search 

Time Complexity: O(M * logN)
Space complexity : O(1)
"""


class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        start, end = 10**6 + 1, 0
        for row in grid:
            start = min(start, row[0])
            end = max(end, row[-1])

        medianCount = len(grid) * len(grid[0]) // 2 + 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.find(grid, mid) >= medianCount:
                end = mid
            else:
                start = mid

        if self.find(grid, end) >= medianCount:
            return end

        return start

    def find(self, grid, median):
        cnt = 0
        for row in grid:
            cnt += self.binarySearch(row, median)

        return cnt

    def binarySearch(self, array, target):
        start, end = 0, len(array) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if array[mid] <= target:
                start = mid
            else:
                end = mid

        if array[end] <= target:
            return end + 1

        if array[start] > target:
            return start

        return start + 1
