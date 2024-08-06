"""
Solution 1:

Traverse

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 1
        depth = max(depth, self.maxDepth(root.left) + 1)
        depth = max(depth, self.maxDepth(root.right) + 1)

        return depth
