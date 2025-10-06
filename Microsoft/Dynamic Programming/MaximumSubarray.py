class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       

        if len(nums) == 1:
            return nums[0]
        
        memo = [float('-inf')]*len(nums)
        memo[0] = nums[0]
        memo[1] = max(nums[1],memo[0]+nums[1])
        for i in range(2,len(nums)):
            memo[i] = max(nums[i],nums[i]+memo[i-1])
        return max(memo)
        
        