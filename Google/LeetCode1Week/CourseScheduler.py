from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for ai, bi in prerequisites:
            graph[bi].append(ai)  # bi -> ai

        visited = [False] * numCourses       # fully explored
        active_path = [False] * numCourses   # current DFS path

        def dfs(node):
            if active_path[node]:  # found a cycle
                return False
            if visited[node]:      # already processed
                return True

            active_path[node] = True
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            active_path[node] = False
            visited[node] = True   # mark fully explored
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
