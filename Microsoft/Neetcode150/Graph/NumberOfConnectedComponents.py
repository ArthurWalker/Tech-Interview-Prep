class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visit = set()
        count=0
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in graph[node]:
                if nei not in visit:
                    dfs(nei)
            return
        
        for node,_nei in graph.items():
            if node not in visit:
                count+=1
                dfs(node)
        return count