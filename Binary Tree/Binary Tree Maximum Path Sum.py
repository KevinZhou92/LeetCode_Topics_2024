"""
Solution 1:

Recursiont

Be careful about negative value

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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.globalMax = -sys.maxsize
        self.findMax(root)

        return self.globalMax

    def findMax(self, root):
        if not root:
            return -sys.maxsize

        leftMax = self.findMax(root.left)
        rightMax = self.findMax(root.right)
        self.globalMax = max(
            self.globalMax,
            leftMax,
            rightMax,
            leftMax + rightMax + root.val,
            leftMax + root.val,
            rightMax + root.val,
            root.val,
        )

        return max(leftMax + root.val, rightMax + root.val, root.val)
