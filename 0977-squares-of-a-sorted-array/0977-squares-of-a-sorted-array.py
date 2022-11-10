class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        l, r = 0, len(nums)-1
        res = []
        
        while l<=r:
            lsq, rsq = nums[l]**2, nums[r]**2
            if lsq>rsq:
                res.append(lsq)
                l+=1
            else:
                res.append(rsq)
                r-=1
        
        return res[::-1]
  