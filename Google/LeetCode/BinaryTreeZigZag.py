# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        level = 0
        res = {}
        while queue:
            level_size = len(queue)
            res[level] = []
            for count in range(level_size):
                node = queue.pop(0)
                res[level].append(node.val)
                if level % 2 == 1 and count == level_size - 1:
                    res[level] = res[level][::-1]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return list(res.values())