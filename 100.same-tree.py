#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Time complexity of solution: O(min(N,M)), where N,M is the number of nodes of the trees p,q
        # Space compexity of solution: O(min(H1, H2)) where H1, H2 is the height of the two trees p,q
        # both are None (return True)
        if p is None and q is None:
            return True
        # one them is None
        elif (p is None) ^ (q is None):
            return False
        # they both exist (check values)
        else:
            check1 = p.val == q.val
            check2 = self.isSameTree(p.left, q.left)
            check3 = self.isSameTree(p.right, q.right)
            return check1 & check2 & check3
            

# @lc code=end

