import collections
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        mp1 = collections.Counter(nums)
        maxfreq = max(mp1.values())
        
        minIdx = {}
        maxIdx = {}
        minLen = {}
        n = len(nums)
        minLen = {}
        for i in range(n):
            
            if mp1[nums[i]]!= maxfreq: continue
              
            minId, maxId = n, -1
            if nums[i] in minIdx:
                minId = minIdx[nums[i]]
            
            if nums[i] in maxIdx:
                maxId = maxIdx[nums[i]]
            
            minIdx[nums[i]] = min(minId, i)
            maxIdx[nums[i]] = max(maxId, i)

            minLen[nums[i]] = maxIdx[nums[i]] - minIdx[nums[i]] + 1
            
        
        return min(minLen.values())
         