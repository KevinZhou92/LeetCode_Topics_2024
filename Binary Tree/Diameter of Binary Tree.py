"""
Solution 1:

Recursion

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.findDiameter(root)[0]

    def findDiameter(self, root):
        if not root:
            return 0, 0

        leftMax, leftPath = self.findDiameter(root.left)
        rightMax, rightPath = self.findDiameter(root.right)

        return (
            max(leftMax, rightMax, leftPath + rightPath),
            max(leftPath, rightPath) + 1,
        )
