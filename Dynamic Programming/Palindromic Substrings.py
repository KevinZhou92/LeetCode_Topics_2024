"""
Solution 1:

Dynamic Programming

Time Complexity: O(n^2)
Space complexity : O(n^2)
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            dp[i][i] = True
            cnt += 1

        for i in range(n - 1):
            if s[i] != s[i + 1]:
                continue
            dp[i][i + 1] = True
            cnt += 1

        for length in range(3, n + 1):
            for i in range(n):
                if (
                    i + length - 1 < n
                    and dp[i + 1][i + length - 2]
                    and s[i] == s[i + length - 1]
                ):
                    dp[i][i + length - 1] = True
                    cnt += 1

        return cnt
