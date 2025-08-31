class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        memo = {}
        
        def findLIS(ind,prev):
            if ind == len(nums):
                return 0
            if (ind,prev) in memo:
                return memo[(ind,prev)]

            max_len = findLIS(ind+1,prev)
            if prev ==float('-inf') or nums[ind] > prev:
                max_len = max(max_len,1 + findLIS(ind+1, nums[ind]))

            memo[(ind,prev)] = max_len
            return max_len

        return findLIS(0,float('-inf'))

        
