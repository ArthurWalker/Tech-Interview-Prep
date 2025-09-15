
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(node,path):
            if not node.left and not node.right:
                path_arrow = '->'.join(path+[str(node.val)])
                if path_arrow not in res:
                    res.append(path_arrow)
                return 
            if node.left:
                dfs(node.left,path+[str(node.val)])
            if node.right:
                dfs(node.right,path+[str(node.val)])
            return
        dfs(root,[])
        return (res)