"""
Solution 1:

Start from the bottom right, since it's the minium in row and largest in col
So we can eliminate search space

Time Complexity: O(m + n)
Space complexity : O(1)
"""


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        4  3  2  -1
        3  2  1  -1
        1  1  -1 -2
        -1 -1 -2 -3
        """

        if not grid:
            return 0

        count = 0
        r, c = len(grid) - 1, 0
        while r >= 0 and c <= len(grid[0]) - 1:
            if grid[r][c] >= 0:
                c += 1
            else:
                count += len(grid[0]) - c
                r -= 1

        return count
