class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        x = set()
        for n in nums:
            if n not in x:
                x.add(n)
            else:
                return True
        
        return False
            
            
        
            
            
       
        