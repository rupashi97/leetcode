'''
Kadane's Algorithm
 Local Max at index i = Max ( A[i], A[i] + local Max at index i-1)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit

    #         O(n2) solution
    #         for i in range(len(prices)-1):
    #             for j in range(i+1, len(prices)):
    #                 profit = max(prices[j]-prices[i],profit, 0)

    #         return profit




