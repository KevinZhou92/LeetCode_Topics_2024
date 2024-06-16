"""
Solution 1:

Find the node to delete, and find the predecessor or successor to replace it, 
use the delete node function itself again to delete the substition node from the subtree


Time Complexity: O(log(N))
Space complexity : O(H), where H is the hight of the tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        
        if root.right:
            new_root = self.find_successor(root)
            new_right_tree = self.deleteNode(root.right, new_root.val)
            new_root.right = new_right_tree
            new_root.left = root.left
            
            return new_root
        elif root.left:
            return root.left
        
        return None
    
    def find_successor(self, root):
        if not root:
            return None

        root = root.right
        while root.left:
            root = root.left
        
        return root
    
    def find_predecessor(self, root):
        if not root:
            return None

        root = root.left
        while root.right:
            root = root.right
        
        return root
        
        

        