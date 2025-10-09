class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
            no empty
            minimum is length 1
            what if all 0 => return 0
            what if all 1 => return 1

            idea is to fill all connected 1 with 0 
            look for 1
            traversal 4 directions with bfs
            if it is 1, replace with 0 so that we dont need to visit again
        """

        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        ROWS, COLS = len(grid),len(grid[0])
        
        def bfs(row,col):
            queue = [(row,col)]
            while queue:
                level_size = len(queue)
                for _ in range(level_size):
                    cell_row,cell_col =queue.pop(0)
                    for dr,dc in directions:
                        new_row,new_col = dr+cell_row,dc+cell_col
                        if 0<= new_row < ROWS and 0<= new_col < COLS and grid[new_row][new_col] == '1':
                            grid[new_row][new_col] = '0'
                            queue.append((new_row,new_col))

        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    bfs(row,col)
                    count+=1
        return count