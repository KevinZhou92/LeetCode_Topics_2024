"""
Solution 1:

UF + BFS

Time Complexity: O(M * N)
Space complexity : O(E)
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        uf = UF(m, n)

        queue = deque([])
        for i in range(m):
            for j in range(n):
                if not grid[i][j] == "1":
                    continue
                queue.append((i, j))

        visited = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                visited.add((r, c))
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    newR, newC = r + dx, c + dy
                    if not self.valid(m, n, newR, newC, visited):
                        continue
                    if grid[newR][newC] == "1":
                        uf.connect(r * n + c, newR * n + newC)
                        queue.append((newR, newC))

        res = set()
        for i in range(m):
            for j in range(n):
                if not grid[i][j] == "1":
                    continue
                res.add(uf.find((i * n + j)))

        return len(res)

    def valid(self, m, n, newR, newC, visited):
        if newR < 0 or newR >= m:
            return False

        if newC < 0 or newC >= n:
            return False

        if (newR, newC) in visited:
            return False

        return True


class UF:
    def __init__(self, m, n):
        self.parents = [0] * m * n
        self.rank = [1] * m * n
        for i in range(m):
            for j in range(n):
                self.parents[i * n + j] = i * n + j
        self.size = len(self.parents)

    def connect(self, x, y):
        pX = self.find(x)
        pY = self.find(y)
        if pX == pY:
            return

        if self.rank[pX] < self.rank[pY]:
            self.parents[pY] = pX
            self.rank[pX] += self.rank[pY]
        else:
            self.parents[pX] = pY
            self.rank[pY] += self.rank[pX]

        self.size -= 1

    def find(self, x):
        root = x
        while root != self.parents[root]:
            root = self.parents[root]

        while x != self.parents[x]:
            parent = self.parents[x]
            self.parents[x] = root
            x = parent

        return root

    def getSize(self):
        return self.size


"""
Solution 2:

BFS

Time Complexity: O(m * N)
Space complexity : O(m * N)
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "1":
                    continue
                num_islands += 1
                queue = deque([(i, j)])
                while queue:
                    x, y = queue.popleft()
                    if (
                        0 <= x < len(grid)
                        and 0 <= y < len(grid[0])
                        and grid[x][y] == "1"
                    ):
                        grid[x][y] = "0"  # mark as visited
                        for dx, dy in directions:
                            queue.append((x + dx, y + dy))

        return num_islands


"""
Solution 3:

DFS

Time Complexity: O(m * n)
Space complexity : O(m * n)
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        numOfIsland = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1":
                    continue
                self.dfs(grid, m, n, i, j)
                numOfIsland += 1

        return numOfIsland

    def dfs(self, grid, r, c, i, j):
        if i < 0 or i >= r or j < 0 or j >= c:
            return

        if grid[i][j] == "0":
            return

        grid[i][j] = "0"
        self.dfs(grid, r, c, i + 1, j)
        self.dfs(grid, r, c, i - 1, j)
        self.dfs(grid, r, c, i, j + 1)
        self.dfs(grid, r, c, i, j - 1)
