class Solution:
    def climbStairs(self, n: int) -> int:
        if n  == 1:
            return 1
        dp = {}
        def dfs(cur_step):
            if cur_step == n:
                return 1
            if cur_step > n:
                return 0
            if (cur_step)  in dp:
                return dp[cur_step] 
            dp[cur_step] = dfs(cur_step+1)+dfs(cur_step+2)
            return dp[cur_step]
        
        return dfs(0)