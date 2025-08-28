class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid),len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        
        def dfs(row,col,cur_area):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == 0:
                return
            
            cur_area.append(1)
            grid[row][col] = 0
            for dr, dc in directions:
                new_r, new_c = dr+row, dc+col
                if ROWS> new_r >= 0 and COLS > new_c>=0 and grid[new_r][new_c]==1:
                    dfs(new_r,new_c,cur_area)
            return

        areas = []
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    area = []
                    dfs(row,col,area)
                    areas.append(area)

        res = [len(a) for a in areas]
        if len(res)==0:
            return 0
        return max(res)