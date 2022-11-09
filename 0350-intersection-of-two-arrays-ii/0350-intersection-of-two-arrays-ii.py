import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        track = collections.defaultdict(int)
        for n in nums1: track[n] += 1

        ans = []
        for n in nums2:
            if track[n]:
                track[n] -=1
                ans.append(n)
        
        return ans
     