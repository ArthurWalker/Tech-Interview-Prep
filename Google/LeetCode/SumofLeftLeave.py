# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        lefttotal = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                cur_node = queue.pop(0)
                if cur_node.left:
                    if (not cur_node.left.left and not cur_node.left.right):
                        lefttotal+=cur_node.left.val
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
        return lefttotal