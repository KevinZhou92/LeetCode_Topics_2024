"""
Solution 1:

Recursion + Prefix Sum

Time Complexity: O(N)
Space complexity : O(N)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        self.count = 0
        self.search(root, 0, targetSum, {})

        return self.count

    def search(self, root, curSum, targetSum, prefixSum):
        if not root:
            return

        curSum += root.val
        if curSum == targetSum:
            self.count += 1

        self.count += prefixSum.get(curSum - targetSum, 0)

        prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        self.search(root.left, curSum, targetSum, prefixSum)
        self.search(root.right, curSum, targetSum, prefixSum)
        prefixSum[curSum] -= 1
