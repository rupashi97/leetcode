from typing import List


# Slow
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


# Little fast
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashmap = {}

        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                return True

        return False






