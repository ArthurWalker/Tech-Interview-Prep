class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows*cols-1
        while left <= right:
            mid = left + (right-left)//2
            mid_l, mid_r = mid // cols, mid % cols
            if target == matrix[mid_l][mid_r]:
                return True
            elif target > matrix[mid_l][mid_r]:
                left = mid +1
            else:
                right = mid-1
        return False