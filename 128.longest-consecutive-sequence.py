#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # This solution is O(N), very smart. Worst case is an array containing a full sequence. In that case we iterate through the array twice (O(2N))        longest = 0 
        num_set = set(nums)

        for n in num_set:
            if (n-1) not in num_set:
                length = 1
                while(n+length) in num_set:
                    length +=1
                longest = max(longest, length)
        return longest
    
# @lc code=end

