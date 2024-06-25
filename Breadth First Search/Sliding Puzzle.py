"""
Solution 1:

BFS

Tricky part:
1. Represent the 2D array using 1D array for easy manipulation of cells
2. Boundary check, For a 2x3 board, moving from an index like 2 (the rightmost cell of the first row) to 3 (the leftmost cell of the second row) 
should be avoided, and similarly for other boundary crossings.

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        if not board:
            return -1

        board = tuple(e for row in board for e in row)
        target = tuple([1, 2, 3, 4, 5, 0])
        queue = deque([board])
        visited = set()
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                board = queue.popleft()
                # pick 1 cell out of 6 to move
                # 0 1 2
                # 3 4 5
                if board == target:
                    return steps
                zero_index = self.find_zero(board)
                for j in (-3, +1, -1, +3):
                    cur = list(board)
                    if not self.move_cell(cur, zero_index, j):
                        continue
                    cur = tuple(cur)
                    if cur not in visited:
                        queue.append(cur)
                        visited.add(cur)
            steps += 1

        return -1

    def find_zero(self, board):
        return [i for i in range(len(board)) if board[i] == 0][0]

    def move_cell(self, board, i, j):
        if i + j < 0 or i + j >= 6:
            return False

        # For a 2x3 board, moving from an index like 2 (the rightmost cell of the first row) to 3 (the leftmost cell of the second row)
        # should be avoided, and similarly for other boundary crossings.
        if i == 3 and i + j == 2 or i == 2 and i + j == 3:
            return False

        board[i], board[i + j] = board[i + j], board[i]

        return True
