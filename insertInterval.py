from typing import List


# 1 Saw solution = Find strictly left and strictly right intervals. Merge all others. Combine and return
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        s, e = newInterval[0], newInterval[1]

        left, right = [], []

        for i in intervals:

            if i[1] < s:
                left.append(i)
            elif e < i[0]:
                right.append(i)
            else:
                s = min(s, i[0])
                e = max(e, i[1])

        return left + [[s, e]] + right


# 2 - Optimized version of #1
class Solution:
    def insert(self, intervals, I):
        res, i = [], -1
        for i, (x, y) in enumerate(intervals):
            if y < I[0]:
                res.append([x, y])
            elif I[1] < x:
                i -= 1
                break
            else:
                I[0] = min(I[0], x)
                I[1] = max(I[1], y)

        return res + [I] + intervals[i + 1:]


# Incomplete solution = Corner cases not handled
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        s, e = newInterval[0], newInterval[1]

        if not intervals:
            intervals.append(newInterval)
            return intervals

        i, k = 0, 0

        for i in range(len(intervals) - 1):
            if intervals[i][0] <= s <= intervals[i + 1][0]:
                break

        for k in range(i + 1, len(intervals)):
            if intervals[k][0] <= e < intervals[k + 1][0]:
                break

        if i == len(intervals) - 1: k = 0

        si, ei = intervals[i][0], intervals[i][1]
        sii, eii = intervals[k][0], intervals[k][1]  # change

        if s <= ei:  # merging with 1st
            if k and sii <= e:  # merging with both
                intervals[i] = [si, max(e, eii)]
                for j in range(i + 1, k + 1):
                    intervals.pop(i + 1)
            else:
                intervals[i] = [si, max(ei, e)]

        elif k and sii <= e:  # merging with 2nd
            intervals[i + 1] = [s, max(e, eii)]

        else:  # no merge
            intervals.insert(i + 1, [s, e])

        return intervals
