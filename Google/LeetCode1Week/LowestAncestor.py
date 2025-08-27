# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node,num,path):
            path.append(node)
            if num > node.val:
                return dfs(node.right,num,path)
            elif num < node.val:
                return dfs(node.left,num,path)
            else:
                return path

        p_path = dfs(root,p.val,[])
        q_path = dfs(root,q.val,[])
        min_len = min(len(p_path),len(q_path))
        i = 0
        while i< min_len:
            if p_path[i].val == q_path[i].val:
                i+=1
            else:
                break
        return p_path[i-1]

            

