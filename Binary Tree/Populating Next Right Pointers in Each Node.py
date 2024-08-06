"""
Solution 1:

BFS - Level Order Traversal

Travers nodes level by level and connect node on the same level

Time Complexity: O(n)
Space complexity : O(n)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return

        queue = deque([root])
        prev = None
        while queue:
            size = len(queue)
            for idx in range(size):
                cur = queue.popleft()
                if idx != 0:
                    prev.next = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                prev = cur
            prev = None

        return root


"""
Solution 2:

Recursively connect node

There are 3 type of nodes we need to connect
1. Node1's left and right child
2. Node2's left and right child
3. Node1's right child and Node2's left child

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return

        self.connect_node(root.left, root.right)

        return root

    def connect_node(self, node1, node2):
        if not node1 or not node2:
            return

        node1.next = node2

        self.connect_node(node1.left, node1.right)
        self.connect_node(node1.right, node2.left)
        self.connect_node(node2.left, node2.right)
