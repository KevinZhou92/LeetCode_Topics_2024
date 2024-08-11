"""
Solution 1:

BFS

Time Complexity: O(m * n)
Space complexity : O(m * n)
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        m = len(grid)
        n = len(grid[0])
        queue = deque([])
        freshOranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshOranges += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        time = 0
        while queue:
            if freshOranges == 0:
                return time
            time += 1
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    newX = x + dx
                    newY = y + dy
                    if 0 <= newX < m and 0 <= newY < n and grid[newX][newY] == 1:
                        freshOranges -= 1
                        grid[newX][newY] = 2
                        queue.append((newX, newY))

        return time if freshOranges == 0 else -1
