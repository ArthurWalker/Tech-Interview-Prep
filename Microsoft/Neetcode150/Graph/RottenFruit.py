class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ROWS, COLS = len(grid),len(grid[0])
        queue = []
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1
        rotten = len(queue)
        level = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                crow, ccol = queue.pop(0)
                for dr, dc in directions:
                    new_row, new_col = dr+crow,dc+ccol
                    if 0<=new_row < ROWS and 0<= new_col < COLS and grid[new_row][new_col] ==1:
                        grid[new_row][new_col] = 2
                        fresh -=1
                        queue.append((new_row,new_col)) 
            level+=1
        if fresh > 0:
            return -1
        return level-1