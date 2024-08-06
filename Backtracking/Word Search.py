"""
Solution 1:

Backtracking, start search from every cell, only search if the cur char matches
with the char in the word

Time Complexity: O(N * 3^L)
Space complexity : O(L)
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False
        
        m = len(board)
        n = len(board[0])
        for r in range(m):
            for c in range(n):
                if not self.search(board, r, c, [], word, 0):
                    continue
                return True
        
        return False
    
    def search(self, board, r, c, cur, word, idx):
        if len(cur) == len(word):
            return True

        if not self.isValidPos(board, r, c):
            return False

        if board[r][c] != word[idx]:
            return False

        curChar = word[idx]
        board[r][c] = "#"
        cur.append(curChar)
        for dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            newR = r + dir[0]
            newC = c + dir[1]
            if self.search(board, newR, newC, cur, word, idx + 1):
                return True
        cur.pop()
        board[r][c] = curChar
        
    def isValidPos(self, board, r, c):
        m = len(board)
        n = len(board[0])
        if r < 0 or r >= m:
            return False
        
        if c < 0 or c >= n:
            return False
        
        if board[r][c] == "#":
            return False
        
        return True
        
        
        if c < 0 or c >= n:
            return False
        
        return True
    
