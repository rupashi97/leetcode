'''
Longest substring without repeating characters

Difference b/w substring and subsequence:
A Substring takes out characters from a string placed between two specified indices in a continuous order.
Subsequence can be derived from another sequence by deleting some or none of the elements in between but
always maintaining the relative order of elements in the original sequence.
'''


# O(n) solution | Done by myself
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        M = 1
        sub = set()
        left = 0

        for x in s:
            if x not in sub:
                sub.add(x)
                continue

            m = len(sub)
            M = max(M, m)

            while x in sub:
                sub.remove(s[left])
                left += 1

            sub.add(x)

        if not s: return 0

        return max(M, len(sub)) # if s=au for example


# O(n^2) | done by myself
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 1
        for i in range(len(s) - 1):
            maxl = 1
            sub = set({s[i]})
            for j in range(i + 1, len(s)):
                if s[j] in sub:
                    break
                sub.add(s[j])
                maxl += 1

            res = max(res, maxl)

        if not s: return 0

        return res