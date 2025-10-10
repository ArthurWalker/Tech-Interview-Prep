class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
            no negative
            no duplicate in prerequisites
            num course > 0
            prerequisite can be empty
            prerequisites unique?
    
            [0,1],[1,2],[2,0] => it has a loop => not possible

            directed graph
            set up the graph using hashmap

            for every node, i will check if it can be finish courses from there:
                i have 2 variables => visited and active path
                    visited to store all visited nodes
                    active is to used to see if it can finish the path
                use dfs to travel along the directed graph. both visit and active has the node
                But actiev will undo the path at the end. If it has a loop, it will never reach the end and 
                the node exists in active => it is wrong. Else, it is not a loop and can return a full path
            if i detect a loop then there is no way i can finish all courses =>return immediately to []
            else: return the []

            edge case:
                prerequisite is empty => return range from 0 to numCourses
                num course = 0 => return []
        """
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]
        if numCourses == 0:
            return []
        
        graph = {i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            graph[b].append(a)
        
        def dfs(node):
            if node in active:
                return True
            if node in visit:
                return False

            visit.add(node)
            active.add(node)
            for neigh in graph[node]:
                loop = dfs(neigh)
                if loop:
                    return True
            active.remove(node)
            output.append(node)
            return False
            
        visit, active = set(), set()
        output = []
        for node in graph.keys():
            is_cycle = dfs(node)
            if is_cycle:
                return []
        return output[::-1]