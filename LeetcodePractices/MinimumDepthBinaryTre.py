# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            
            if not root.right:
                return 1+ self.minDepth(root.left)
            if not root.left:
                return 1+ self.minDepth(root.right)
            return 1+ min(self.minDepth(root.left),self.minDepth(root.right))

        def bfs(root):
            if not root:
                return 0

            queue = [root]
            level= 1
            while queue:
                level_size = len(queue)
                for _ in range(level_size):
                    curr_node = queue.pop(0)
                    if not curr_node.left and not curr_node.right:
                        return level
                    if curr_node.left:
                        queue.append(curr_node.left)
                    if curr_node.right:
                        queue.append(curr_node.right) 
                level +=1
            return level

        return bfs(root)