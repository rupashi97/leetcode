class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        b = 0
        l = len(nums)-1
        
        while b<=l:
            m = (b+l)//2
            if target == nums[m]:
                return m
            
            if target>nums[m]:
                b = m+1
            else: l = m-1
                
        return -1    
                
        