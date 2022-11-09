class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        b, l = 0, len(nums)-1
        idx = 0
        
        while b<=l:
            m = (b+l)//2
            
            if target==nums[m]:
                return m
            
            if target<nums[m]:
                l=m-1
            else: b = m+1
            
        
        return b
        