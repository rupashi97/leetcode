from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        track = Counter(nums)

        for i in track.keys():
            if track[i] > len(nums) / 2:
                return i
