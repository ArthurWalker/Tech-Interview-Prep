class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
            all 1 => row*col
            all 0 => 0
            how many seperated islands in the grid? Could be more than 1 
            if it is 1 big island


            use BFS
            loop for rows in len 1 -> rows-1
                loop for col in len 1 -> cols-1:
                    if found 1 => traver 4 directions, increase max_area by 1 and replace 1 to 0 
        """

        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        def bfs(row,col):
            max_area = 1
            queue = [(row,col)]
            grid[row][col] = 0
            while queue:
                level_size = len(queue)
                for _ in queue:
                    cell_row, cell_col = queue.pop(0)
                    for dr,dc in directions:
                        new_row,new_col = dr+cell_row,dc+cell_col
                        if 0 <= new_row < ROWS and 0<= new_col < COLS and grid[new_row][new_col] == 1:
                            grid[new_row][new_col] = 0
                            max_area+=1
                            queue.append((new_row,new_col))
            return max_area

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    area = bfs(row,col)
                    max_area = max(max_area,area)
        
        return max_area