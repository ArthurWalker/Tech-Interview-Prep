# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
            Traversal then sort
            then find min in that sorted list
            time comlexity will be NlogN
        """
        queue = [root]
        lst = []
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr = queue.pop(0)
                lst.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        lst.sort()
        min_diff = float("inf")
        for i in range(1, len(lst)):
            min_diff = min(min_diff, lst[i] - lst[i-1])

        return min_diff