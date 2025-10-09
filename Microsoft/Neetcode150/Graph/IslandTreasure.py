class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
            what if all -1 => 0
            what if all 0 => 0
            what if all INF => INF

            iterate through the grid, if found 0:
                save to queue
            
            Starting queue
                
        """

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        queue = []
        # Step 1: Start BFS from all treasures (0s)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                row,col = queue.pop(0)
                for dr,dc in directions:
                    nrow,ncol = dr+row,dc+col
                    if 0 <= nrow < ROWS and 0 <= ncol < COLS and grid[nrow][ncol] == INF:
                        grid[nrow][ncol] = 1+ grid[row][col]
                        queue.append((nrow,ncol))