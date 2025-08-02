# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res  = {}
        level = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr_node = queue.pop(0)
                if level not in res:
                    res[level] = [curr_node.val]
                else:
                    res[level].append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            level+=1
        
        return list(res.values())