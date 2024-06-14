"""
Solution 1:

Bottm up approach.

Invert left substree and right subtree and exchange left and right subtree for root node


Time Complexity: O(n)
Space complexity : O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        tmp = root.left # this is very important, we need to make sure we capture the original left child
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)

        return root

"""
Solution 1:

Top down approach

Time Complexity: O(n)
Space complexity : O(n)
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        self.invert(root)

        return root
    
    def invert(self, root):
        if not root:
            return

        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invert(root.left)
        self.invert(root.right)
        
        