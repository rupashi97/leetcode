import collections
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        minsarr = [None]*(amount+1)
        
        def minCoins(amount):
            
            if amount==0: return 0 
            
            if amount<0: return -1 
            
            if minsarr[amount]: return minsarr[amount]
            
            minVal = float('inf')
            for coin in coins:
                val = minCoins(amount-coin)
                if val==-1: continue
                minVal = min(minVal, val+1)
                
            
            if minVal == float('inf'): 
                minsarr[amount]= -1
            else: minsarr[amount] = minVal
            
            return minsarr[amount]
        
        return minCoins(amount)
                 