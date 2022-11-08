class Solution:
    def maxProfit(self, prices: List[int]) -> int:

#         minPrice = float('inf')
#         maxProfit = 0
        
#         for i in range(len(prices)):
#             minPrice = min(minPrice, prices[i])
#             diff = prices[i]-minPrice
#             maxProfit = max(maxProfit, diff)
            
#         return maxProfit

        localMax = 0
        maxProfit = 0
        for i in range(1, len(prices)):
            localMax = max(prices[i]-prices[i-1], localMax + prices[i]-prices[i-1])
            maxProfit = max(maxProfit, localMax)
            
            
        return maxProfit 