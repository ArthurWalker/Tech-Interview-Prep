class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board),len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(row,col,region):
            if row < 0 or row >=ROWS or col < 0 or col >= COLS or board[row][col] == 'X' or (row,col) in visited:
                return
            visited.add((row,col)) 
            
            region.append((row,col))

            for dr,dc in directions:
                new_r, new_c = dr+row, dc+col
                if 0 <= new_r < ROWS and 0<= new_c< COLS and board[new_r][new_c] == 'O':
                    dfs(new_r,new_c,region)
            return

        visited = set()
        areas = []
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O' and (row,col) not in visited:
                    region = []
                    dfs(row,col,region)
                    areas.append(region)
        def check_legit(area):
            for row,col in area:
                if row == ROWS-1 or col == COLS-1 or row == 0 or col == 0:
                    return False
            return True
        for area in areas:
            if len(area)>0 and check_legit(area):
                for row,col in area:
                    board[row][col] = 'X'