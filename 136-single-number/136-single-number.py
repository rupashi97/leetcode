class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        track = collections.Counter(nums)
        
        for k in track.keys():
            if track[k]==1:
                return k
        
        