"""
Solution 1:

Recursion.

Be careful about picking the index of the current depth

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        self.traverse(root, res, 0)

        return res

    def traverse(self, root, res, depth):
        if not root:
            return

        if len(res) == depth:
            res.append([])

        res[depth].append(root.val)
        self.traverse(root.left, res, depth + 1)
        self.traverse(root.right, res, depth + 1)


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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])
        while queue:
            size = len(queue)
            res.append([])
            for _ in range(size):
                cur = queue.popleft()
                res[-1].append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return res
