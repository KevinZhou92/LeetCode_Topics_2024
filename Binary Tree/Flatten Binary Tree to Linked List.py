"""
Solution 1:

Pre-order traversal.

While doing pre order traversal, we always return the tail of the subtree, so we can then
tweak the left and right subtree of the current root node and flatten the tree.

Notice it's not always a complete tree so we need to be careful about corner case:
1. cur root node has no left and right sub trees
2. cur root node only has left sub tree
3. cur root node only has right sub tree

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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 

        self.flatten_tree(root)
        
        return
    
    def flatten_tree(self, root):
        if not root:
            return None

        if not root.left and not root.right:
            return riit
       
        left_tail = self.flatten_tree(root.left)
        right_tail = self.flatten_tree(root.right)
        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None
        
        if right_tail:
            return right_tail

        return left_tail


"""
Solution 2:

Recursively connect node

There are 3 type of nodes we need to connect
1. Node1's left and right child
2. Node2's left and right child
3. Node1's right child and Node2's left child

Time Complexity: O(n)
Space complexity : O(n)
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        self.connect_node(root.left, root.right)

        return root
    
    def connect_node(self, node1, node2):
        if not node1 or not node2:
            return
        
        node1.next = node2

        self.connect_node(node1.left, node1.right)
        self.connect_node(node1.right, node2.left)
        self.connect_node(node2.left, node2.right)