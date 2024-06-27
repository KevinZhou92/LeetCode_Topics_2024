"""
Solution 1:

Write the code to generate the matrix clock wise, just to make sure we don't overlap written array


Time Complexity: O(N^2)
Space complexity : O(N^2)
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []

        res = [[0 for _ in range(n)] for _ in range(n)]
        count = 0
        up = 0
        down = n - 1
        left = 0
        right = n - 1
        while count < n * n:
            for i in range(left, right + 1):
                count += 1
                res[up][i] = count

            for i in range(up + 1, down + 1):
                count += 1
                res[i][right] = count

            if up != down:
                for i in range(right - 1, left - 1, -1):
                    count += 1
                    res[down][i] = count

            if left != right:
                for i in range(down - 1, up, -1):
                    count += 1
                    res[i][left] = count

            up += 1
            down -= 1
            left += 1
            right -= 1

        return res
