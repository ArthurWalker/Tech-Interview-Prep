class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        if target > nums[right]:
            return right+1
        if target < nums[left]:
            return left

        mid = 0
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                left = mid+1
            else:
                right = mid -1
        return left