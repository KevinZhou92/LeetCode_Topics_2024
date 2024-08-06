"""
Solution 1:

DFS

Time Complexity: O(N)
Space complexity : O(N)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        self.traverse(root, res, 0)

        return res

    def traverse(self, root, res, depth):
        if not root:
            return

        if len(res) == depth:
            res.append(root.val)

        self.traverse(root.right, res, depth + 1)
        self.traverse(root.left, res, depth + 1)


"""
Solution 2:

BFS

Time Complexity: O(N)
Space complexity : O(N)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        res = []
        while queue:
            size = len(queue)
            res.append(queue[size - 1].val)
            for _ in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return res
