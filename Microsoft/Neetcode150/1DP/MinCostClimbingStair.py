class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
            cost not empty and >= 2
            no negative
            could have dup

            dynamic bottom up

            take step 1 or step 2
            if i ==n => finished
            compare min betwen step 1 or step 2

            [1,2,3] 
            n = 3 => 2
            dp[0] = 0
            dp[1] = 0
            dp[2] = min(cost[0]+dp[0],cost[1]+dp[1]) = (1,2) = 1
            dp[3] = min(cost[i-2]+dp[i-2],cost[i-1]+dp[i-1]) = 2+0 = 2

            dp = [0]*(n+1)

        """
        dp = [0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            dp[i] = min(cost[i-2]+dp[i-2],cost[i-1]+dp[i-1])
        return dp[len(cost)]