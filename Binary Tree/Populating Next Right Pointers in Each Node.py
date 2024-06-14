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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
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
        