class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        minPrice = prices[0]
        
        for i in range(1, len(prices)):
            minPrice = min(prices[i], minPrice)
            currMax = prices[i] - minPrice
            maxProfit = max(maxProfit, currMax)
            
        return maxProfit
            