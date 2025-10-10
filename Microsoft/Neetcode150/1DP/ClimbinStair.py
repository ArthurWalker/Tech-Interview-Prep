class Solution:
    def climbStairs(self, n: int) -> int:
        """
            n not negative
            n != 0

            n = 2
            1 1
            2 

            n = 3
            1 1 1
            1 2
            2 1
            => 3

            2 path:
            1 and 2
            1 2   1 2
            finish at if equal to n

            try to use dynamic programming
            dp = [0]*n
            dp[1] = 1
            dp[2] = 2
            for i in range(3,n):
                dp[i] = dp[i-1]+dp[i-2]
                dp[3] = dp[2] + dp[1] = 2 + 1 =3 
                dp[2] = 2
                dp[1] = 1
                dp[0] = 0
            => return dp[n] = ?
        """
        if n <= 2:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        print(dp)
        return dp[n]
