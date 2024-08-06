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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, preorder, pL, pR, inorder, iL, iR):
        if pL > pR or iL > iR:
            return None

        root = TreeNode(preorder[pL])
        indexOfRoot = self.findIndex(inorder, preorder[pL])
        root.left = self.build(
            preorder, pL + 1, pL + (indexOfRoot - iL), inorder, iL, indexOfRoot - 1
        )
        root.right = self.build(
            preorder, pL + (indexOfRoot - iL) + 1, pR, inorder, indexOfRoot + 1, iR
        )

        return root

    def findIndex(self, inorder, target):
        return inorder.index(target)
