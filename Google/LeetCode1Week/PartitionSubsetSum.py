class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        memo = {}
        def recursion(ind,target):
            if ind >= len(nums):
                return target ==0
            if target <0:
                return False
            if (ind,target) in memo:
                return memo[(ind,target)]
            memo[(ind,target)]=  recursion(ind+1,target) or recursion(ind+1,target-nums[ind])
            return memo[(ind,target)]

        return recursion(0,sum(nums)//2)  