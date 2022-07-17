'''
Given the root of a binary tree, return the length of the diameter of the tree.

Diameter: length of the longest path between any two nodes in a tree

Logic : Dfs
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global d
        d = 0

        def depth(node):
            global d
            if not node:
                return 0

            l = depth(node.left)
            r = depth(node.right)
            d = max(d, l + r)

            return 1 + max(l, r)

        depth(root)

        return d

