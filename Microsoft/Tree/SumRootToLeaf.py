# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def sumNumbers(self, root: Optional[TreeNode]) -> int:
#         if not root.left and not root.right:
#             return root.val
        
#         res = set()
#         def backtrack(node,path):
#             if not node:
#                 return
#             path += str(node.val)
#             if not node.left and not node.right:
#                 res.add(int(path))
#                 return
#             backtrack(node.left,path)
#             backtrack(node.right,path)
            
#         backtrack(root,'')
#         return sum(list(res))


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        def backtrack(node, path):
            nonlocal total
            if not node:
                return
            path = path * 10 + node.val  # build number as int directly
            
            # leaf
            if not node.left and not node.right:
                total += path
                return
            
            backtrack(node.left, path)
            backtrack(node.right, path)

        backtrack(root, 0)
        return total
