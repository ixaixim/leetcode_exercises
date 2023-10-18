#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Do a binary search of the matrix by listing its elements from 0 to m*n-1 
        # Time complexity: O(logm + logn) = O(log(m*n))
        # Space complexity: O(1)
        m = len(matrix)
        n = len(matrix[0]) 
        left = 0 
        right = m*n-1
        while left<=right:
            mid = (left+right)//2
            row = mid//n
            col = mid%n
            if target > matrix[row][col]:
                left = mid+1
            elif target < matrix[row][col]:
                right = mid-1
            else:
                return True
        return False
# @lc code=end

