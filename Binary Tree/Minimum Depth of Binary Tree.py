"""
Solution 1:

DFS
One tricky thing is if the left or right child is none we should not consider the depth
from a null child.


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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        leftMin = self.minDepth(root.left)
        rightMin = self.minDepth(root.right)

        if leftMin == 0:
            return rightMin + 1
        
        if rightMin == 0:
            return leftMin + 1

        return min(leftMin + 1, rightMin + 1)

"""
Solution 2:

BFS

Level order traversal, return min depth if current node has no child, which means it is a leaf node

Time Complexity: O(N)
Space complexity : O(N)
"""
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        minDepth = 0
        while queue:
            size = len(queue)
            minDepth += 1
            for _ in range(size):
                node = queue.popleft()
                if not node.left and not node.right:
                    return minDepth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return minDepth
        