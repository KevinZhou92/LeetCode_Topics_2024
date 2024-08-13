"""
Solution 1:

Use first row and first col of Matrix to mark if there is 0 in current row or col


Time Complexity: O(m * N)
Space complexity : O(1)
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        m = len(matrix)
        n = len(matrix[0])
        isFirstColZero = False
        isFirstRowZero = False

        # Determine if the first row or first column needs to be zeroed
        for i in range(m):
            if matrix[i][0] == 0:
                isFirstColZero = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                isFirstRowZero = True
                break

        # Use the first row and first column as markers for other rows and columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out cells based on markers in the first row and first column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out the first row if needed
        if isFirstRowZero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero out the first column if needed
        if isFirstColZero:
            for i in range(m):
                matrix[i][0] = 0
