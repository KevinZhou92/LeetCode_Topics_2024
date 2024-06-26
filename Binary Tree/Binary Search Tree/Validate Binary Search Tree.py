"""
Solution 1:

Recursion.

BST:
1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.

Time Complexity: O(H)
Space complexity : O(H)
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.valid_BST(root, -sys.maxsize, sys.maxsize)
       
    
    def valid_BST(self, root, min_val, max_val):
        if not root:
            return True
        
        if root.left and root.val <= root.left.val:
            return False
        
        if root.right and root.val >= root.right.val:
            return False
        
        if root.val >= max_val or root.val <= min_val:
            return False

        valid_left = self.valid_BST(root.left, min_val, root.val)
        valid_right = self.valid_BST(root.right, root.val, max_val)
        
        return valid_left and valid_right

"""
Solution 2:

Iterative Solution. Keep track of previous node in inorder traversal and check if previous value is 
greater than the current value

BST in-order traversal is always ascending order

Time Complexity: O(H)
Space complexity : O(1)
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        prev = None
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and prev.val >= root.val:
                return False
            prev = root
            root = prev.right
        
        return True
            
            
