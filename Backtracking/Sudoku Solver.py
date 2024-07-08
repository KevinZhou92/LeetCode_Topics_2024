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

"""
Solution 2:

Use Space to reduce time complexity
Use map for each row, col, box to track used numbers, this can reduce time complexity for 
isValid function to O(1)

Time Complexity: O()
Space complexity : O()
"""
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.rows = [defaultdict(int) for _ in range(9)]
        self.cols = [defaultdict(int) for _ in range(9)]
        self.boxes = [defaultdict(int) for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                boxIndex = (r // 3) * 3 + c // 3
                self.putNumber(board, r, c, boxIndex, int(board[r][c]))

        return self.search(board, 0, 0)
    
    def search(self, board, r, c):
        if r == len(board):
            return True
        
        if c == len(board[r]):
            return self.search(board, r + 1, 0)
        
        if board[r][c] != ".":
            return self.search(board, r, c + 1)
        else:
            boxIndex = (r // 3) * 3 + c // 3
            for candidate in range(1, 10):
                if not self.isValid(board, r, c, boxIndex, candidate):
                    continue
                self.putNumber(board, r, c, boxIndex, candidate)
                if self.search(board, r, c + 1):
                    return True
                self.removeNumber(board, r, c, boxIndex, candidate)
                board[r][c] = "."

        return False
    
    def putNumber(self, board, r, c, boxIndex, candidate):
        self.rows[r][candidate] = 1
        self.cols[c][candidate] = 1
        self.boxes[boxIndex][candidate] = 1
        board[r][c] = str(candidate)

    def removeNumber(self, board, r, c, boxIndex, candidate):
        self.rows[r].pop(candidate)
        self.cols[c].pop(candidate)
        self.boxes[boxIndex].pop(candidate)
        board[r][c] = '.'

    def isValid(self, board, row, col, boxIndex, candidate):
        return not (candidate in self.rows[row] 
            or candidate in self.cols[col]
            or candidate in self.boxes[boxIndex])