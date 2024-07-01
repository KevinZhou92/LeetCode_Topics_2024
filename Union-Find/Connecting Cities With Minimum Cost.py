"""
Solution 1:

Union-Find + Kruskal's algorithm

Time Complexity: O(N to be the total number of nodes (cities) and M to be the total number of edges (connections). 
Sorting all the M connections will take O(M⋅logM). 
Performing union find each time will take log ∗N (Iterated logarithm). 
Hence for M edges, it's O(M⋅log∗N) which is practically O(M) as the value of iterated logarithm, log∗N never exceeds 5.)
Space complexity : O(N)
"""


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        if not connections:
            return 0

        connections.sort(key=lambda conn: conn[2])
        res = 0
        uf = UF(n)
        for conn in connections:
            p1, p2, weight = conn
            if uf.isConnected(p1 - 1, p2 - 1):
                continue
            uf.connect(p1 - 1, p2 - 1)
            res += weight
            if uf.getCount() == 1:
                return res

        return res if uf.getCount() == 1 else -1


class UF:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.count = n

    def find(self, p1):
        if self.parents[p1] == p1:
            return p1
        self.parents[p1] = self.find(self.parents[p1])

        return self.parents[p1]

    def connect(self, p1, p2):
        root1 = self.find(p1)
        root2 = self.find(p2)

        if root1 == root2:
            return

        if self.size[root1] < self.size[root2]:
            self.parents[root2] = root1
            self.size[root1] += self.size[root2]
        else:
            self.parents[root1] = root2
            self.size[root2] += self.size[root1]

        self.count -= 1

    def isConnected(self, p1, p2):
        root1 = self.find(p1)
        root2 = self.find(p2)

        return root1 == root2

    def getCount(self):
        return self.count
