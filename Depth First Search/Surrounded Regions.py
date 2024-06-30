"""
Solution 1:

DFS
Search from borders, mark all 'O' that is connected to border cells with 'E'

Loopo of the board again, mark all escaped cells as 'X', mark all 'O' as X

Time Complexity: O(R * C)
Space complexity : O(R * C)
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(board)
        cols = len(board[0])
        borders = list(product(range(rows), [0, cols - 1])) + list(product([0, rows - 1], range(cols)))
        
        for r, c in borders:
            if board[r][c] != "O":
                continue
            self.search(board, r, c, dirs)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'E':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':  
                    board[r][c] = 'X'

        return

    def search(self, board, r, c, dirs):
        if r < 0 or r > len(board) - 1 or c < 0 or c > len(board[0]) - 1:
            return

        if board[r][c] == 'X':
            return
        
        if board[r][c] == 'E':
            return
        
        board[r][c] = 'E'
        for dr, dc in dirs:
            newR = r + dr
            newC = c + dc
            self.search(board, newR, newC, dirs)

"""
Solution 2:

BFS

Time Complexity: O(N) N is number of cells
Space complexity : O(N)
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(board)
        cols = len(board[0])
        borders = list(product(range(rows), [0, cols - 1])) + list(product([0, rows - 1], range(cols)))
        visited = set(borders)
        
        queue = deque(borders)
        while queue:
            r, c = queue.popleft()
            if board[r][c] != 'O':
                continue
            board[r][c] = 'E'
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newR = r + dr
                newC = c + dc
                if newR < 0 or newR > rows - 1 or newC < 0 or newC > cols - 1:
                    continue
                if (newR, newC) in visited:
                    continue
                if board[newR][newC] != 'O':
                    continue
                visited.add((newR,newC))
                queue.append((newR, newC))
        print(board)


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'E':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':  
                    board[r][c] = 'X'

        return