# @before-stub-for-debug-begin
from python3problem704 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Sol from https://leetcode.com/problems/binary-search/solutions/3363885/easy-solutions-in-java-python-and-c-look-at-once-with-exaplanation/
        left = 0 
        right = (len(nums)-1)
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else: 
                left = mid + 1
        return -1
    
        # continue splitting the array in half and searching.
        # note: my solution allocates unnecessary memory since it assigns a new array every time. 
        # My sol: 
        # while True:
        #     N = len(nums)//2
        #     if nums[N] <  target:
        #         nums = nums[N+1:]
        #     elif nums[N] > target:
        #         nums = nums[:N]
        #     elif nums[N] == target:
        #         return N
        #     else: 
        #         return -1
# @lc code=end

