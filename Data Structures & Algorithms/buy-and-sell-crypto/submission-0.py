class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        seenMin, i, profit = prices[0], 0, 0
        if n <= 1:
            return 0
        for i in range(n):
            seenMin = min(prices[i], seenMin)
            profit = max(prices[i] - seenMin, profit)
            
            
        return profit
