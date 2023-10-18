#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        el_to_index = {}
        for i, el in enumerate(nums):
            el2 = target - el
            if el2 in el_to_index:
                return [i, el_to_index[el2]]
            else:
                el_to_index[el] = i
            
# @lc code=end

