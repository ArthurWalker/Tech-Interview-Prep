class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ROWS, COLS = len(matrix),len(matrix[0])
        visited = {}
        find_zeroes = []
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    find_zeroes.append((row,col))
        zeroes_row =set()
        zeroes_col = set()
        for coor_row, coor_col in find_zeroes:
            if coor_row not in zeroes_row:
                zeroes_row.add(coor_row)
                for col in range(COLS):
                    matrix[coor_row][col] = 0
            if coor_col not in zeroes_col:
                zeroes_col.add(coor_col)
                for row in range(ROWS):
                    matrix[row][coor_col] = 0