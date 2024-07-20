"""
Solution 1:

Binary Search

A trick is to define the search space use the minimum possiblie value and the maximum possible value

Time Complexity: O(NlogM), where N is length of pile, m is the large speed we would search
Space complexity : O(1)
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return -1

        # start speed and end speed
        # find the first speed that can satisfy the time requirement
        start, end = 1, max(piles)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.canFinish(piles, mid, h):
                end = mid
            else:
                start = mid

        if self.canFinish(piles, start, h):
            return start

        if self.canFinish(piles, end, h):
            return end

        return -1

    def canFinish(self, piles, speed, h):
        totalTime = 0
        for pile in piles:
            if pile % speed != 0:
                totalTime += pile // speed + 1
            else:
                totalTime += pile // speed

        return totalTime <= h
