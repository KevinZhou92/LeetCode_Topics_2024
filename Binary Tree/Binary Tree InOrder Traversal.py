"""
Solution 1:

Recursion

Time Complexity: O(H)
Space complexity : O(H)
"""
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        self.inorder_traverse(root, result)

        return result
    
    def inorder_traverse(self, root, result):
        if not root:
            return
        
        self.inorder_traverse(root.left, result)
        result.append(root.val)
        self.inorder_traverse(root.right, result)

"""
Solution 2:

Iterative. Simulate Stack

Time Complexity: O(H)
Space complexity : O(1)
"""
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        stack = []
        cur = root
        prev = None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right

        
        return result