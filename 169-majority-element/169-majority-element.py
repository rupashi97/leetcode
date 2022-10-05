from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
        hashTable = Counter(nums)  # O(n)
        
        maj  = int(len(nums)/2)
        
        for key,val in hashTable.items(): # O(n)
            if val>maj:
                maj=val
                k = key
                
        
        return k
            