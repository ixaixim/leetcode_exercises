# @before-stub-for-debug-begin
from python3problem347 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from collections import defaultdict
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequency (O(n))
        freq = defaultdict(int)
        for num in nums: 
            freq[num] += 1
        
        # sort by frequency (O(nlogn))
        result = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        return list(result.keys())[:k]
# Total time complexity: O(n) + O(nlogn) = O(nlogn)


# @lc code=end

