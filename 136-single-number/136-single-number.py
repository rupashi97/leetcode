class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        track = collections.defaultdict(int)
        
        for n in nums:
            track[n]+=1
        
        for k in track.keys():
            if track[k]==1:
                return k
        
        