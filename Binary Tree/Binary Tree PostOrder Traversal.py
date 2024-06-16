"""
Solution 1:

Recursion

Time Complexity: O(H)
Space complexity : O(H)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        self.postorder_traversal(root, res)

        return res
    
    def postorder_traversal(self, root, res):
        if not root:
            return
        
        self.postorder_traversal(root.left, res)
        self.postorder_traversal(root.right, res)
        res.append(root.val)

"""
Solution 2:

Iterative Solution

Time Complexity: O(H)
Space complexity : O(H)
"""
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack: 
                if prev != stack[-1].right:
                    root = stack[-1].right
                    prev = root
                else:
                    prev_root = stack.pop()
                    res.append(prev_root.val)
                    root = None
                    prev = prev_root
                    
        return res
        
        