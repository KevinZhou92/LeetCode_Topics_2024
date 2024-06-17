"""
Solution 1:

Backtracking to find all possible DISTINCT solutions for placing queens

Time Complexity: O(n!)
Space complexity : O(n)
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []

        res = []
        self.place_queens(n, 0, [], res)

        return self.build_board(res, n)
    
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
    

    def build_board(self, queens, n):
        res = []
        for queen in queens:
            cur_res = []
            for row in range(n):
                cur_row = [ '.' if queen[row] != idx else 'Q' for idx in range(n)]
                cur_res.append(''.join(cur_row))
            res.append(cur_res)
        
        return res
    