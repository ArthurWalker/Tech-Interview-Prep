class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            nine_digit = [s for s in board[i] if s != '.']
            if len(nine_digit) != len(set(nine_digit)):
                return False

        nine_digit = []        
        for i in range(9):
            for j in range(9):
                if board[j][i]!='.':
                    nine_digit.append(board[j][i])
            if len(nine_digit)  != len(set(nine_digit)):
                return False
            nine_digit = []

        nine_digit = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                for m in range(3):
                    for n in range(3):
                        if board[i+m][j+n]!='.':
                            nine_digit.append(board[i+m][j+n])
                if len(nine_digit)!=len(set(nine_digit)):
                    return False
                nine_digit = []
        return True
