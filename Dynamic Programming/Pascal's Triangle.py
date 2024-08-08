"""
Solution 1:

DP

Time Complexity: O(n ^ 2)
Space complexity : O(n ^ 2)
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []

        res = []
        for r in range(1, numRows + 1):
            cur = []
            for i in range(r):
                cur.append(1)
                if r > 2 and i > 0 and i < r - 1:
                    cur[i] = res[-1][i] + res[-1][i - 1]
            res.append(cur)

        return res
