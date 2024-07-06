"""
Solution 1:

Backtracking Fill in cells 1 by 1

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        return self.search(board, 0, 0)

    def search(self, board, r, c):
        if r == len(board):
            return True

        if c == len(board[r]):
            return self.search(board, r + 1, 0)

        if board[r][c] != ".":
            return self.search(board, r, c + 1)
        else:
            for candidate in range(1, 10):
                if not self.isValid(board, r, c, str(candidate)):
                    continue
                board[r][c] = str(candidate)
                if self.search(board, r, c + 1):
                    return True
                board[r][c] = "."

        return False

    def isValid(self, board, row, col, candidate):
        for i in range(9):
            if board[i][col] == candidate:
                return False
            if board[row][i] == candidate:
                return False

            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == candidate:
                return False

        return True
