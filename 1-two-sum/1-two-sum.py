from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        hash_table = defaultdict(int)
        
        for i in range(len(nums)):
            res = target - nums[i]
            
            if res in hash_table:
                return [hash_table[res], i]
            
            hash_table[nums[i]]=i
            
                
            
            