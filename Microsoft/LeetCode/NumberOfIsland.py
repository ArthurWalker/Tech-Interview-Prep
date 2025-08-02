class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        ROWS, COLS = len(grid), len(grid[0])
        island_num = 0

        def dfs(r,c):
            if r < 0 or c< 0 or r >= ROWS or c >= COLS or grid[r][c] == '0':
                return

            grid[r][c] = '0'
            for direc_r,direc_c in directions:
                new_r,new_c = r+direc_r,c+direc_c
                if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c]=='1':
                    dfs(new_r,new_c)
            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] =='1':
                    island_num+=1
                    dfs(r,c)


        return island_num 



