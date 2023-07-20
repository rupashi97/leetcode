class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        mindiff = float('inf') # O(nlogn)
        
        for i in range(len(nums)-k+1): # O(k)
            diff = nums[i+k-1]-nums[i]
            mindiff = min(mindiff, diff) 
            
        return mindiff
            
        