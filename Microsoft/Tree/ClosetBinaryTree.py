# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return 0
        
        while root:
            print(root.val)
            if root.val < target:
                return root.val
            if target >= root.val:
                root = root.right
            else:
                root = root.left
        
        