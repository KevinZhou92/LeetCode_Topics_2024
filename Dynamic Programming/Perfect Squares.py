"""
Solution 1:

DP

Time Complexity: O(n * sqrt(n))
Space complexity : O(n)
"""


class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0

        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            maxCan = math.floor(math.sqrt(i))
            for j in range(1, maxCan + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)

        return dp[-1]
