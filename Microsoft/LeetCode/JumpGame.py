class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True  # The last index is always reachable from itself

        for i in range(n - 2, -1, -1):
            furthest = min(i + nums[i], n - 1)
            for j in range(i + 1, furthest + 1):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]
