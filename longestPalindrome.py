'''
Find length of longest palindrome that can be formed from s

s = "abccccdd"
output = 7 | "dccaccd"
'''
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:

        track = Counter(s)
        flag, size = 0, 0

        for i in track.values():
            if not i % 2:  # even
                size += i
            else:  # odd
                flag = 1
                size += i - 1

        return flag + size


class Solution2:
    def longestPalindrome(self, s: str) -> int:

        table = set()
        for c in s:
            if c not in table:
                table.add(c)
            else:
                table.remove(c)

        return len(s) - len(table) + 1 if len(table) > 0 else len(s)




