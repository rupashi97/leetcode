'''
Balanced Binary Tree = HARD

Defn: a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Solution: DFS = Depth First Search
        Traverse till bottom and work your way up via recursion ~ Traverse first / Condition later
        At every lower level find out the height
        -1 will indicate if at that root and below, the tree is not balanced
        0 ~ zero height as no node present
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check(root):
            if root is None:
                return 0

            left, right = check(root.left), check(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return check(root) != -1



