class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = prices[0]
        maxProfit = 0
        
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            diff = prices[i]-minPrice
            maxProfit = max(maxProfit, diff)
            
        return maxProfit
            