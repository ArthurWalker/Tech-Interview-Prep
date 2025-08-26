# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.dia = 0
    
    def postorder(self,root):
        if root == None:
            return 0
        left = self.postorder(root.left)
        right = self.postorder(root.right)
        
        self.dia = max(self.dia,left+right) # compare current depth with stored depth
        print('Val',root.val)
        if root.left:
            print('Left val',root.left.val,left)
        if root.right:
            print('Right val',root.right.val,right)
        print('Dia',self.dia)
        print('HIHIHIHIH')
        return 1+ max(left,right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
            Every time passing a node, save the longest path to that node from bottom
            Then continue to calculate the longest path of each node
        """
        self.postorder(root)
        return self.dia