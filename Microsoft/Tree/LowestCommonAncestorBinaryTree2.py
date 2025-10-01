"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ppath = []
        while p:
            ppath.append(p)
            p = p.parent
        qpath = []
        while q:
            qpath.append(q)
            q = q.parent
        
        ppath = ppath[::-1]
        qpath = qpath[::-1]

        i = 0
        while i < min(len(ppath),len(qpath)) and ppath[i].val == qpath[i].val:
            i+=1
        return ppath[i-1]