class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
            find the whole island
            if cell is 0 or at the edge then increase by 1
        """
        ROWS, COLS = len(grid),len(grid[0])
        
        def bfs(row,col):
            peri = 0
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            visited = {(row,col):True}
            queue = [(row,col)]
            
            while queue:
                level_size = len(queue)
                for edja in range(level_size):
                    curr_row,curr_col = queue.pop(0)
                    for dr,dc in directions:
                        newr,newc = dr+curr_row,dc+curr_col
                        if 0<=newr<ROWS and 0 <=newc<COLS and grid[newr][newc] == 1 and (newr,newc) not in visited:
                            visited[(newr,newc)]=True
                            queue.append((newr,newc))
                        else:
                            if (newr,newc) not in visited:
                                peri+=1
            return peri


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return bfs(row,col)