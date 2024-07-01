"""
Solution 1:

Union-Find

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        if not equations:
            return False

        uf = UF(equations)
        for e in equations:
            if e[1] != "=":
                continue
            if uf.isConnected(e[0], e[3]):
                continue
            uf.connect(e[0], e[3])

        for e in equations:
            if e[1] != "!":
                continue
            if uf.isConnected(e[0], e[3]):
                return False

        return True


class UF:
    def __init__(self, equations):
        for e in equations:
            self.parents[e[0]] = e[0]
            self.parents[e[3]] = e[3]
            self.size[e[0]] = 1
            self.size[e[3]] = 1

    def connect(self, p1, p2):
        root1 = self.find(p1)
        root2 = self.find(p2)

        if self.size[root1] < self.size[root2]:
            self.parents[root2] = root1
            self.size[root1] += self.size[root2]
        else:
            self.parents[root1] = root2
            self.size[root2] += self.size[root1]

    def find(self, p1):
        root = p1
        while root != self.parents[root]:
            root = self.parents[root]

        oldParent = self.parents[p1]
        while p1 != self.parents[p1]:
            self.parents[p1] = root
            p1 = oldParent
            oldParent = self.parents[oldParent]

        return root

    def isConnected(self, p1, p2):
        root1 = self.find(p1)
        root2 = self.find(p2)

        return root1 == root2
