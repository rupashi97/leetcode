'''
Recursion problem

Approach : Depth-first search
'''

from typing import List


# Very slow
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        def subFill(image, sr, sc, color, start):
            if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]):
                return image

            if image[sr][sc] == start:
                image[sr][sc] = color
                subFill(image, sr - 1, sc, color, start)
                subFill(image, sr + 1, sc, color, start)
                subFill(image, sr, sc - 1, color, start)
                subFill(image, sr, sc + 1, color, start)

        start = image[sr][sc]
        subFill(image, sr, sc, color, start)

        return image


# Slight better
class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        m, n = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image

        def subFill(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: subFill(r - 1, c)
                if r < m - 1: subFill(r + 1, c)
                if c >= 1: subFill(r, c - 1)
                if c < n - 1: subFill(r, c + 1)

        subFill(sr, sc)
        return image


# Fastest
class Solution3:
    def floodFill(self, image, sr, sc, newColor):
        def dfs(i, j):
            image[i][j] = newColor
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                    dfs(x, y)
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor:
            dfs(sr, sc)
        return image
