class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board),len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def dfs(row,col,word_ind,visit):
            if word_ind == len(word)-1:
                return True
            
            for dr, dc in directions:
                new_r,new_c = dr+row,dc+col
                if 0 <= new_r < ROWS and 0<= new_c < COLS and board[new_r][new_c] == word[word_ind+1] and (new_r,new_c) not in visit:
                    visit.append((new_r,new_c))
                    matched = dfs(new_r,new_c,word_ind+1,visit)
                    if matched:
                        return True
                    visit.pop()
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    visit = [(i,j)]
                    matched = dfs(i,j,0,visit)
                    if matched:
                        return True
        return False