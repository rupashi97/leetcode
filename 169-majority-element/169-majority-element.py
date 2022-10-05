from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
        hashTable = Counter(nums)  # O(n)
        
        n = len(nums)
        
        for key,val in hashTable.items(): # O(n)
            if val > n/2:
                return key
