class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        p = [1] * len(nums)
        s = [1] * len(nums)
        ans=[]
        
        for i in range(1, len(nums)):
            p[i] = p[i-1]*nums[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            s[i] = s[i+1]*nums[i+1]
        
        for i in range(len(nums)):
            ans.append(p[i]*s[i])
        # print(p,s)
        return ans
                          