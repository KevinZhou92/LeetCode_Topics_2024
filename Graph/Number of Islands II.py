"""
Solution 1:

UF

Time Complexity: O(m * n)
Space complexity : O(m * n)
"""


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        if not positions:
            return 0

        uf = UF(m, n)
        visited = set()
        res = []
        for pos in positions:
            r, c = pos
            if (r, c) in visited:
                res.append(uf.getSize())
                continue
            uf.increment()
            visited.add((r, c))
            if (r + 1, c) in visited:
                uf.connect(r * n + c, (r + 1) * n + c)
            if (r - 1, c) in visited:
                uf.connect(r * n + c, (r - 1) * n + c)
            if (r, c + 1) in visited:
                uf.connect(r * n + c, r * n + c + 1)
            if (r, c - 1) in visited:
                uf.connect(r * n + c, r * n + c - 1)
            res.append(uf.getSize())

        return res

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
        self.size = 0

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

    def increment(self):
        self.size += 1
