# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSameTree(self,q:Optional[TreeNode],p:Optional[TreeNode]) -> bool:
        if p == q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            if  (p.val == q.val):
                return self.isSameTree(p.left,q.left) and self.isSameTree(q.right,p.right)
            else:
                return False
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == subRoot == None:
            return True
        elif root == None:
            return False
        else:
            if self.isSameTree(root,subRoot):
                return True
            
            left = self.isSubtree(root.left,subRoot)
            right = self.isSubtree(root.right,subRoot)
            return left or right
       