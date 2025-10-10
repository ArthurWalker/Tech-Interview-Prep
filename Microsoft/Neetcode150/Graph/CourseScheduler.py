class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
            Directed graph
            all positives
            numCourse >=1
            len of each pre is 2
            no duplicates
            each item is from 0 to numCourse
            not linear 

            define a graph
            you can finish if it is continuous line and have no cycle
            =>  detect cycle
            dfs travel
            visited path = nodes that are visited
            check_complete_path = nodes that are visited and complete. If check exist a previous node, that is wrong
            => it will be true if Check path is True else False

            [[0,1],[1,2],[1,3], [2,4],[3,4]] => finished
            [[0,1],[1,2],[1,3], [3,0],[3,4]] => Flase
        """
        if len(prerequisites) == 1:
            return True
        
        graph = {i:[] for i in range(numCourses)}
        for item in prerequisites:
            graph[item[1]].append(item[0])

        visit, active = set(),set()
        def dfs(node):
            if node in active:
                return True
            if node in visit:
                return False

            visit.add(node)
            active.add(node)
            for neighbor in graph[node]:
                detected_loop = dfs(neighbor)
                if detected_loop:
                    return True
            active.remove(node)
            return False

        for c in range(numCourses):
            is_cycle = dfs(c)
            if is_cycle:
                return False
        return True
        

        

