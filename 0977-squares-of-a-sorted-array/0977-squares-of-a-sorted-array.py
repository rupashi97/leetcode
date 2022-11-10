class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        l, r = 0, n-1
        res = [0] * n
        
        for i in range(n-1, -1, -1):
            lsq, rsq = nums[l]**2, nums[r]**2
            if lsq>rsq:
                res[i] = lsq
                l+=1
            else:
                res[i] = rsq
                r-=1
        
        return res
  