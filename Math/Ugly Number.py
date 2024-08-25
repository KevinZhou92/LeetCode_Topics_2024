"""
Solution 1:

Math

Time Complexity: O(logN)
Space complexity : O(1)
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 5 == 0:
            n /= 5
        while n % 3 == 0:
            n /= 3
        while n % 2 == 0:
            n /= 2

        return n == 1
