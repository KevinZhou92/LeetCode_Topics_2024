"""
Solution 1:

Recursion

Time Complexity: O(N)
Space complexity : O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root:
            return None

        return self.search(root, p, q)

    def search(self, root, p, q):
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left = self.search(root.left, p, q)
        right = self.search(root.right, p, q)

        if left and right:
            return root

        if left:
            return left

        if right:
            return right

        return None
