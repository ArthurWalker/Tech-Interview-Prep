class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count_fresh = 0
        count_rotten = 0
        rotten_coor = []
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    count_fresh += 1
                elif grid[i][j] == 2:
                    count_rotten += 1
                    rotten_coor.append((i, j))

        if count_rotten == count_fresh == 0:
            return 0
        if count_rotten == 0:
            return -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = rotten_coor
        minute = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                rotten_cell = queue.pop(0)
                for dir_r, dir_c in directions:
                    new_r, new_c = dir_r + rotten_cell[0], dir_c + rotten_cell[1]
                    if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        count_fresh -= 1
                        count_rotten += 1
                        queue.append((new_r, new_c))
            minute += 1
        if count_fresh != 0:
            return -1
        return minute - 1