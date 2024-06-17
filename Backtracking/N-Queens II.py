"""
Solution 1:

Backtracking

Time Complexity: O(n!)
Space complexity : O(n)
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return []

        res = []
        self.place_queens(n, 0, [], res)

        return len(res)
    
    def place_queens(self, n, row, queens, res):
        if row == n:
            res.append([q for q in queens])
            return
        
        for col in range(n):
            if not self.is_valid(n, row, col, queens):
                continue
            queens.append(col)
            self.place_queens(n, row + 1, queens, res)
            queens.pop()
    
    def is_valid(self, n, row, col, queens):
        if row >= n or row < 0 or col < 0 or col >= n:
            return False
        
        if col in queens:
            return False
        
        for r in range(len(queens)):
            if abs(r - row) / abs(col - queens[r]) == 1:
                return False
        
        return True

"""
Solution 2:

Backtracking bottom up

Time Complexity: O(n!)
Space complexity : O(n)
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return []

        return self.place_queens(n, 0, [])

    
    def place_queens(self, n, row, queens):
        if row == n:
            return 1
        
        solutions = 0
        for col in range(n):
            if not self.is_valid(n, row, col, queens):
                continue
            queens.append(col)
            solutions += self.place_queens(n, row + 1, queens)
            queens.pop()
        
        return solutions
    
    def is_valid(self, n, row, col, queens):
        if row >= n or row < 0 or col < 0 or col >= n:
            return False
        
        if col in queens:
            return False
        
        for r in range(len(queens)):
            if abs(r - row) / abs(col - queens[r]) == 1:
                return False
        
        return True
