# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 1
        queue = [(root,0)]
        max_size = 0
        while queue :
            level_size = len(queue)
            for _ in range(level_size):
                node, index = queue.pop(0)
                if node.left:
                    queue.append((node.left,2*index))
                if  node.right:
                    queue.append((node.right,2*index+1))
            if queue:
                max_size = max(max_size,queue[-1][-1]-queue[0][-1]+1)
        return max_size