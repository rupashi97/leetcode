class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        size = len(nums)
        flag = False
        for i in range(size-2, -1, -1):
                if nums[i] < nums[i+1]:

                    idx = size-1
                    for j in range(i+1, size):
                        if nums[j]<=nums[i]: 
                            idx = j-1
                            break

                    nums[i], nums[idx] = nums[idx],  nums[i]
                    nums[i+1:] = sorted(nums[i+1:])
                    flag = True
                    break
        
        if not flag:
            nums.reverse()