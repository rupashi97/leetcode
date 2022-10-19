import collections
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        mp = collections.defaultdict(int)
        
        for i in range(len(nums)):
            k = target - nums[i]
            
            if k in mp:
                return [i, mp[k]]
            
            mp[nums[i]]=i
            
            
                