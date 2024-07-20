"""
Solution 1:

Search a 2D matrix, flatten the index to convert it to a binary search issue

Time Complexity: O(log(R * C))
Space complexity : O(1)
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])
        start, end = 0, row * col - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            r, c = self.getIndex(mid, row, col)
            if matrix[r][c] < target:
                start = mid
            else:
                end = mid

        r, c = self.getIndex(start, row, col)
        if matrix[r][c] == target:
            return True
        r, c = self.getIndex(end, row, col)
        if matrix[r][c] == target:
            return True

        return False

    def getIndex(self, pos, row, col):
        return pos // col, pos % col
