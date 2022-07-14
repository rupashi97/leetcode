'''
Simple string problem
Construct ransomNote from magazine

ransomNote = aa
magazine = aab
output = true

ransomNote = aa
magazine = ab
output = false
'''

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        tracker = Counter(magazine)
        for i in ransomNote: tracker[i] -= 1
        return all(x >= 0 for x in tracker.values())
