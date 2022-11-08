import collections
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        track = collections.defaultdict(int)
        
        for i in range(len(nums)):
            x = target - nums[i]
            if x in track:
                return [i, track[x]]
            
            track[nums[i]]=i      
                      