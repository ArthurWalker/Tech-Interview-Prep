class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        memo = [-1 for i in range(len(nums))]
        def depth_first_search(po):
            if po >= len(nums):
                return 0
            elif po == len(nums)-1:
                return nums[po]
            if memo[po]!=-1:
                return memo[po]
            else:
                memo[po] = max(nums[po]+depth_first_search(po+2),depth_first_search(po+1))
            return memo[po]


        return depth_first_search(0)

