"""
Solution 1:

Union Find

Note: Check if two components are connected before connect them and decrease the count

Time Complexity: O(V + E)
Space complexity : O(V + E)
"""


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return count

        uf = UF(n)
        for edge in edges:
            if uf.isConnected(edge[0], edge[1]):
                continue
            uf.connect(edge[0], edge[1])

        return uf.count


class UF:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.count = n

    def find(self, p1):
        root = p1
        while root != self.parents[root]:
            root = self.parents[root]

        oldParent = self.parents[p1]
        while p1 != self.parents[p1]:
            self.parents[p1] = root
            p1 = oldParent
            oldParent = self.parents[p1]

        return root

    def connect(self, p1, p2):
        root1 = self.find(p1)
        root2 = self.find(p2)

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

    def count(self):
        return self.count
