class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(r,c):
            if r > m-1 or c > n-1:
                return 0
            elif r == m-1 and c == n-1:
                return 1
            else:
                if (r,c) not in memo:
                    memo[(r,c)] = dfs(r+1,c)+dfs(r,c+1)
                return memo[(r,c)]

        res = dfs(0,0)
        return res
