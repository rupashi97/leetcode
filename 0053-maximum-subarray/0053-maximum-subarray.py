class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = nums[0]
        largeSum = nums[0]
        for i in range(1, len(nums)):
            largeSum = max(nums[i], nums[i]  + largeSum)
            maxSum = max(largeSum, maxSum)
            
        return maxSum
            
        