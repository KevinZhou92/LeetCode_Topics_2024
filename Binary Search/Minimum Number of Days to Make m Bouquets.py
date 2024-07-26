"""
Solution 1:

Binary Search

Time Complexity: O(NLogC)
Space complexity : O(1)
"""


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        start, end = min(bloomDay), max(bloomDay)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.canWork(bloomDay, m, k, mid):
                end = mid
            else:
                start = mid

        if self.canWork(bloomDay, m, k, start):
            return start

        if self.canWork(bloomDay, m, k, end):
            return end

        return -1

    def canWork(self, array, bouquetNeeded, flowerNeeded, minimumDays):
        bouquetMade = 0
        flowers = 0
        for i in range(len(array)):
            if array[i] > minimumDays:
                flowers = 0
            else:
                flowers += 1

            if flowers == flowerNeeded:
                flowers = 0
                bouquetMade += 1

        return bouquetMade >= bouquetNeeded
