class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        memo = {}
        
        def dfs(r,c):
            if r > ROWS-1 or c  > COLS-1 or obstacleGrid[r][c]==1:
                return 0
            elif r == ROWS-1 and c == COLS-1:
                return 1
            else:
                if (r,c) not in memo:
                    memo[(r,c)] = dfs(r+1,c)+dfs(r,c+1)
                return memo[(r,c)]
        
        res = dfs(0,0)
        return res