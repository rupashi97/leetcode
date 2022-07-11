'''
Invert Binary Tree

A Binary Tree is a tree data structure in which each node has at most two children

Example -
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Trick example
Input: [1,null,2]
Output: [1,2]

'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        temp = root.left
        root.left = root.right
        root.right = temp

        Solution.invertTree(self, root.left)
        Solution.invertTree(self, root.right)

        return root
