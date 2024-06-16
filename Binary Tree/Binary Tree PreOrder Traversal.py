"""
Solution 1:

Recursion

Time Complexity: O(H)
Space complexity : O(H)
"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        self.preorder_traversal(root, res)

        return res

    def preorder_traversal(self, root, res):
        if not root:
            return

        res.append(root.val)
        self.preorder_traversal(root.left, res)
        self.preorder_traversal(root.right, res)        

"""
Solution 2:

Iterative

Time Complexity: O(H)
Space complexity : O(1)
"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = []
        prev = None
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop().right
        
        return res