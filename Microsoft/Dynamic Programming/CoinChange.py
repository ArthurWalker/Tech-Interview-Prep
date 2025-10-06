# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount == 0:
#             return 0
#         if len(coins) == 1:
#             return 1 if coins[0] == amount else -1
        
#         res = []
#         def dfs(ind, temp_comb, curr_val):
#             if curr_val == 0:
#                 res.append(temp_comb[:])
#                 return
#             if curr_val < 0:
#                 return

#             for coin in coins:
#                 temp_comb.append(coin)
#                 dfs(ind+1,temp_comb,curr_val-coin)
#                 temp_comb.pop()
        
#         dfs(0,[],amount)
#         lst_ways = [len(item) for item in res]
#         return min(lst_ways)
        
# class Solution:
#     def coinChange(self, coins: list[int], amount: int) -> int:
#         memo = {}
        
#         def solve(rem):
#             if rem < 0:
#                 return -1
#             if rem == 0:
#                 return 0
#             if rem in memo:
#                 return memo[rem]
            
#             min_count = float('inf')
            
#             for coin in coins:
#                 res = solve(rem - coin)
#                 if res != -1:
#                     min_count = min(min_count, 1 + res)
            
#             memo[rem] = min_count if min_count != float('inf') else -1
#             return memo[rem]
            
#         return solve(amount)

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # dp[i] will be storing the minimum number of coins required for amount i
        # amount + 1 is a placeholder for infinity
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
                    
        return dp[amount] if dp[amount] != amount + 1 else -1