class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
            not empty board or word

            loop through each cell, find if the cell is the first letter of word
                perform the backtrack trace
                    go 4 directions
                    and go back 

                if found the same => return True
                if reach the out of board return False
        """
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ROWS, COLS = len(board),len(board[0])
        path = set()

        def dfs(row,col,word_ind):
            if word_ind == len(word):
                return True
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or board[row][col] != word[word_ind] or (row,col) in path:
                return False
            path.add((row,col))
            res = (dfs(row+1,col,word_ind+1) or dfs(row-1,col,word_ind+1) or  dfs(row,col+1,word_ind+1) or dfs(row,col-1,word_ind+1))
            path.remove((row,col))
            return res
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    res = dfs(row,col,0)
                    if res:
                        return True
        return False