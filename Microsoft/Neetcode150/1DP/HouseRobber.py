class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            because you cant rob 2 adjacent house => it means that you can start rob first house or 2nd house
            and there is has no reason to skip the first 2 house or next 2 house because why waste money 
            0
           1  1
          3 3 3
         4   4 4
            i will do DN top down
            traver until reach the end of the house
            use dfs
        """

        if len(nums) == 1:
            return nums[0]
        dp = {}
        def dfs(ind):
            if ind >= len(nums):
                return 0
            if ind in dp:
                return dp[ind]
            left = dfs(ind+1)
            right = nums[ind] + dfs(ind+2)
            dp[ind] = max(left,right)
            return dp[ind]
        return dfs(0)