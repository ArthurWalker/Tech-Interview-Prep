class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
            two pointers left and right at 0 and len(heights)-1
            as long as left <= right:
                move left when heights left < right because there will be a chance where left heights is higher than right
                move right when heights left > right the same go
                compare the max_area
        """ 

        left, right = 0, len(heights)-1
        max_area = 0
        while left < right:
            max_area = max(max_area,min(heights[left],heights[right])*(right-left))
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return max_area