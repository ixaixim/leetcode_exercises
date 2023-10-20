# @before-stub-for-debug-begin
from python3problem235 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # idea: recall the definition of BST. For subtree values: left_subtree_values < node_value < right_subtree_values
        # if both p,q are smaller than root, then LCA must be in left subtree
        # if both p,q are larger than root, then LCA must be in right subtree
        # if one is smaller and one is larger, then root is LCA
        # Complexity of 'recursive' approach:
        # Time: O(N) where N min(depth(p), depth(q))
        # Space: O(N), since we open a new function and store root,p,q each time we go down one level
        # if p.val > q.val:
        #     p, q = q, p
        # if p.val < root.val and q.val < root.val:
        #     # move down the subtree in case 
        #     return self.lowestCommonAncestor(root.left, p, q)
        # elif p.val > root.val and q.val > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # # return root in case p<=root<=q
        # return root
    
        # better solution from:https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solutions/64963/3-lines-with-o-1-space-1-liners-alternatives/
        # uses 'iterative' approach instead
        # is same as previous approach, but simply reassigns root var.
        # Space complexity: O(1)
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root
# @lc code=end

