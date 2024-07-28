"""
Solution 1:

Binary Search

Time Complexity: O(logN)
Space complexity : O(1)
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        while start + 1 < end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid

        if isBadVersion(start):
            return start

        return end
