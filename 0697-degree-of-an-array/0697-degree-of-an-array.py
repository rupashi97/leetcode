import collections
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        left, right = {},{}
        count = collections.defaultdict(int)
        
        for i, x in enumerate(nums):
            if x not in left: left[x]=i
            right[x] = i
            count[x] += 1
            
        degree = max(count.values())
        minlen = len(nums)
        
        for x in nums:
            if count[x]==degree:
                minlen = min(minlen, right[x] - left[x] + 1)
                
        return minlen
                
        