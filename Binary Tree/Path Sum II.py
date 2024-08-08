"""
Solution 1:

Recursion

Time Complexity: O(N^2)
Space complexity : O(N)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        self.search(root, targetSum, [], res)

        return res

    def search(self, root, targetSum, cur, res):
        if not root:
            return

        if not root.left and not root.right and targetSum == root.val:
            path = [v for v in cur]
            path.append(root.val)
            res.append(path)
            return

        cur.append(root.val)
        self.search(root.left, targetSum - root.val, cur, res)
        self.search(root.right, targetSum - root.val, cur, res)
        cur.pop()
