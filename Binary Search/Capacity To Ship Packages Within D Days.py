"""
Solution 1:

Binary Search

Time Complexity: O(NLogK) K is the gap between max weight and total weight
Space complexity : O(1)
"""


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if not weights:
            return 0

        start, end = max(weights), sum(weights)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.canShip(weights, days, mid):
                end = mid
            else:
                start = mid

        if self.canShip(weights, days, start):
            return start

        return end

    def canShip(self, weights, days, capacity):
        curLoad, daysNeeded = 0, 1
        for w in weights:
            if curLoad + w > capacity:
                curLoad = w
                daysNeeded += 1
            else:
                curLoad += w

        return True if daysNeeded <= days else False
