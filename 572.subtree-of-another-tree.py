#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # solution from https://leetcode.com/problems/subtree-of-another-tree/solutions/265239/python-easy-to-understand/
        # Time complexity of solution: O(N*M), where N,M is the number of nodes of the trees root,subRoot
        if not root: 
            # we reach one of the leaves of the root tree, nothing to compare
            return False
        if self.isSameTree(root, subRoot): 
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p:TreeNode, q: TreeNode) -> bool:
        if p and q:
            # check if the values are the same and if the left and right subtrees are the same
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # return True if both are None, otherwise False
        return p is q
    
# @lc code=end

