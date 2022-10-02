class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1] * len(nums)
        s = 1
        
        for i in range(1, len(nums)):
            ans[i] = ans[i-1]*nums[i-1]
            
        for i in reversed(range(len(nums)-1)):
            ans[i] = ans[i] * nums[i+1] * s
            s *= nums[i+1]
              
        return ans                   