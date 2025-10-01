# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def averageOfSubtree(self, root: TreeNode) -> int:
        '''
            Traversal along the tree
            at each point, calculate  the average because we return curr_sum,curr_count 
        '''
        def traversal(node):
            if not node:
                return 0,0
            
            left = traversal(node.left)
            right = traversal(node.right)

            cur_sum = node.val + left[0] + right[0]
            cur_count = 1 + left[1] + right[1]
            aver = cur_sum // cur_count
            if aver == node.val:
                self.count+=1
            return cur_sum, cur_count
        
        traversal(root)
        return self.count
            