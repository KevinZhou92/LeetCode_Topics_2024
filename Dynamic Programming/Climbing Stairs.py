"""
Solution 1:

DP

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for s in range(2, n + 1):
            dp[s] = dp[s - 2] + dp[s - 1]

        return dp[n]
