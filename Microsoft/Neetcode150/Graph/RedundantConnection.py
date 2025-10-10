class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def dfs(node,par):
            if node in visit:
                return True
            visit.add(node)
            for nei in graph[node]:
                if nei != par:
                    loop = dfs(nei,node)
                    if loop:
                        return True
            return False
        
        
        graph = {i:[] for i in range(len(edges)+1)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            visit = set()
            if dfs(a,-1):
                return [a,b]
        return []