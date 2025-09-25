class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        max_days = 0
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            max_days = max(max_days,prices[right]-prices[left])
        return max_days