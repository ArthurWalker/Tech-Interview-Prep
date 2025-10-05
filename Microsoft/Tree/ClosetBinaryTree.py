# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closet = root.val
        
        while root:
            curr_diff = abs(root.val-target)
            closet_diff = abs(closet - target)
            if curr_diff < closet_diff or (curr_diff == closet_diff and root.val < closet):
                closet = root.val

            if target >= root.val:
                root = root.right
            else:
                root = root.left
        
        return closet
        
        