"""
Solution 1:

Binary Search

Time Complexity: O(sqrt(C) * LogC)
Space complexity : O(1)
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True

        for i in range(math.ceil(math.sqrt(c))):
            if self.search(c - i**2, math.ceil(math.sqrt(c))):
                return True

        return False

    def search(self, target, maxValue):
        start, end = 1, maxValue
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid**2 > target:
                end = mid
            elif mid**2 < target:
                start = mid
            else:
                return True

        if start**2 == target:
            return True

        if end**2 == target:
            return True

        return False
