"""
Solution 1:

BFS

Note that we need to make sure we only have one copy for a single node!

Time Complexity: O(N + M)
Space complexity : O(N)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        newRoot = Node(node.val, [])

        # old, new
        queue = deque([node])
        copied = {node: newRoot}
        while queue:
            cur = queue.popleft()
            copyNode = copied[cur]
            for n in cur.neighbors:
                if n not in copied:
                    copied[n] = Node(n.val, [])
                    queue.append(n)
                copyNode.neighbors.append(copied[n])

        return copied[node]

        return newRoot


"""
Solution 1:

DFS

Time Complexity: O(N)
Space complexity : O(N)
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        return self.cloneNodes(node, {})

    def cloneNodes(self, node, nodeMap):
        if node in nodeMap:
            return nodeMap[node]

        newNode = Node(node.val, [])
        nodeMap[node] = newNode
        for n in node.neighbors:
            newNode.neighbors.append(self.cloneNodes(n, nodeMap))

        return newNode
