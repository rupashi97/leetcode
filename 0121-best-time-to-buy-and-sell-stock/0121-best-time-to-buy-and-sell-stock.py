class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
#         maxProfit = 0
#         minPrice = prices[0]
        
#         for i in range(1, len(prices)):
#             minPrice = min(prices[i], minPrice)
#             currMax = prices[i] - minPrice
#             maxProfit = max(maxProfit, currMax)
            
#         return maxProfit
        
        localMax = 0
        maxProfit = 0
        for i in range(1, len(prices)):
            localMax = max(prices[i]-prices[i-1], localMax + prices[i]-prices[i-1])
            maxProfit = max(localMax, maxProfit)
            
            
        return maxProfit