"""
Solution 1:

DP

Calculate the minimum path sum for each cell

Time Complexity: O(m * n)
Space complexity : O(m * n)
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for c in range(n):
            dp[0][c] = grid[0][c]
            if c > 0:
                dp[0][c] += dp[0][c - 1]

        for r in range(m):
            dp[r][0] = grid[r][0]
            if r > 0:
                dp[r][0] += dp[r - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]


"""
Solution 1:

DP 1D Array

Time Complexity: O(m * n)
Space complexity : O(n)
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                if i == 0 and j > 0:
                    dp[j] = dp[j - 1] + grid[i][j]
                if j == 0 and i > 0:
                    dp[j] = dp[j] + grid[i][j]
                if i > 0 and j > 0:
                    dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]

        return dp[n - 1]
