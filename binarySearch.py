'''
Binary Search algorithm : O(log n)

Array sorted in increasing order
To find: target

'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        begin = 0
        end = len(nums) - 1

        while begin <= end:

            mid = int((begin + end) / 2)
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                begin = mid + 1
            else:
                end = mid - 1

        return -1
