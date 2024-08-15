"""
Solution 1:

n & (n - 1) to remove the least significant 1

Time Complexity: O(1) since the bit is maximum 32/64
Space complexity : O(1)
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n != 0:
            n = n & (n - 1)
            res += 1

        return res
