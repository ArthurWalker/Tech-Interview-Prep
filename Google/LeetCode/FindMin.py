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
        left = right = float('inf')
        if not root.left:
            return 1 + minDepth
        if root.right:
            right = self.minDepth(root.right)
        min_depth = min(left,right) 
        return 1+min_depth