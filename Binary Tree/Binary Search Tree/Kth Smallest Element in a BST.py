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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        res = []
        self.traverse(root, res)

        return res[k - 1]

    def traverse(self, root, res):
        if not root:
            return

        self.traverse(root.left, res)
        res.append(root.val)
        self.traverse(root.right, res)


"""
Solution 2:

Iterative

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

        return 0
