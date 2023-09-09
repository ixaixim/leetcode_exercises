# @before-stub-for-debug-begin
from python3problem238 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from collections import defaultdict
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # the solution: compute products of array elements by iterating forward and backward
        forw_prod = defaultdict(lambda: 1)
        back_prod = defaultdict(lambda: 1)
        n = len(nums) 
        result = []
        
        for i in range(n):
            if i-1<0:
                el = 1
            else: 
                el = nums[i-1]
            forw_prod[i] = forw_prod[i-1] * el

        for i in reversed(range(n)):
            if i+1>n-1:
                el = 1
            else:
                el = nums[i+1]
            back_prod[i] = back_prod[i+1] * el
        for i in range(n):
            result.append(forw_prod[i] * back_prod[i])

        # one- liner solution
        # pre, suf, n = list(accumulate(nums, mul)), list(accumulate(nums[::-1], mul))[::-1], len(nums)
        # return [(pre[i-1] if i else 1) * (suf[i+1] if i+1 < n else 1) for i in range(n)]

            
        return result
# @lc code=end

