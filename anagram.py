'''
Find if t is a valid anagram of s

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

'''
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        htable = {}

        if len(s) != len(t):
            return False

        for c in s:
            htable[c] = htable[c] + 1 if c in htable else 1

        for x in t:
            if x in htable and htable[x] > 0:
                htable[x] = htable[x] - 1
            else:
                return False

        return True


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = collections.Counter(s)
        for x in t: tracker[x] -= 1

        return not any(tracker.values())
