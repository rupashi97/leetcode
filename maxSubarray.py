'''
Find contiguous subarray which has the largest sum
~  Use kadane's algorithm
'''

from typing import List


# Slow
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localMax = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            localMax = max(nums[i], nums[i] + localMax)
            maxSum = max(localMax, maxSum)

        return maxSum


# Slight fast
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])

        return max(nums)









