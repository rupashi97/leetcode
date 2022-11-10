
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k>n: k = k%n
        res = nums[n-k:] + nums[0:n-k]
        
        for i in range(n):
            nums[i] = res[i]
            
            
    