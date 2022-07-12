'''
Lowest Common Ancestor of a Binary Search Tree

Binary Search tree (BST) : Sorted binary tree i.e.
  left nodes < root < right nodes

Lowes Common Ancestor (LCA) :
The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself).
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Slow : Recursion
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root

        elif p == root or q == root:
            return root

        if p.val < root.val:
            return Solution.lowestCommonAncestor(self, root.left, p, q)

        else:
            return Solution.lowestCommonAncestor(self, root.right, p, q)


# Better looking
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        while root:
            if root.val > max(p.val, q.val):
                root = root.left

            elif root.val < min(p.val, q.val):
                root = root.right

            else:
                return root
