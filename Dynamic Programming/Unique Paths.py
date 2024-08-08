"""
Solution 1:

Dynamic Programming

Time Complexity: O(m * n)
Space complexity : O(m * n)
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for c in range(n):
            dp[0][c] = 1

        for r in range(m):
            dp[r][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
