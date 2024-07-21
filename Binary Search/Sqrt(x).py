"""
Solution 1:

Binary Search

Edge Case 

Time Complexity: O(logN)
Space complexity : O(1)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid * mid <= x:
                start = mid
            else:
                end = mid

        if end * end - x <= 0:
            return end

        return start
