#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # have two arrays traverse from the beginning and the end and increase depending on sum value.
        N = len(numbers)
        i = 0
        j = N - 1
        while i < N-1:
            while j > 0:
                if numbers[i] + numbers[j] > target:
                    j-=1
                elif numbers[i] + numbers[j] < target:
                    i+=1
                else:
                    return [i+1, j+1]
            
# @lc code=end

