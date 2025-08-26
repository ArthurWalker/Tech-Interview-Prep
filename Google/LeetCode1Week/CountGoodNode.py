# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The idea is to use traversal each node with preorder, flag 1 if it meets the condition else flag 0
# then we can use that flag to update the count

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def preorder(root,max_node):
            if not root:
                return 0
            if root.val >= max_node:
                count=1
                max_node = root.val
            else:
                count=0
            count += preorder(root.left,max_node)
            count += preorder(root.right,max_node)
            return count
            
        res = preorder(root,root.val)
        return res