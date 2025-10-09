class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
            ["X","X","X","X"],
            ["X","T","X","O"],
            ["X","T","T","X"],
            ["X","T","X","O"]

            travel across the board, find O
            find connected Os 
            if one of them hit the wall => do not replace and cancel
            if none hit any wall => replace
        """

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ROWS, COLS = len(board), len(board[0])
        queue = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or
                        c == 0 or c == COLS - 1 and
                        board[r][c] == "O"
                    ):
                    queue.append((r,c))
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                crow, ccol = queue.pop(0)
                if board[crow][ccol] == 'O':
                    board[crow][ccol] = 'T'
                    for dr, dc in directions:
                        newr,newc = dr+crow,dc+ccol
                        if 0<= newr < ROWS and 0<= newc < COLS:
                            queue.append((newr,newc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"