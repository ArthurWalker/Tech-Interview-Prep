class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image),len(image[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        curr_cor = image[sr][sc]
        if curr_cor == color:
            return image

        image[sr][sc] = color
        queue = [(sr,sc)]
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr_row,curr_col = queue.pop(0)
                for drow, dcol in directions:
                    newr, newc = curr_row+drow, curr_col+dcol
                    if 0 <= newr < ROWS and 0 <= newc < COLS and image[newr][newc] == curr_cor:
                        image[newr][newc]=color
                        queue.append((newr,newc))
        return image                    