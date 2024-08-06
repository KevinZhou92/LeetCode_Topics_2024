"""
Solution 1:

PreOrder Traversal to build the tree

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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        return self.buildTree(nums, 0, len(nums) - 1)

    def buildTree(self, nums, l, r):
        if l > r:
            return None

        midIndex = l + (r - l) // 2
        root = TreeNode(nums[midIndex])
        root.left = self.buildTree(nums, l, midIndex - 1)
        root.right = self.buildTree(nums, midIndex + 1, r)

        return root
