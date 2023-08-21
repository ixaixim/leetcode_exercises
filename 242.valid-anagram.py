# @before-stub-for-debug-begin
from python3problem242 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
from collections import defaultdict

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        for char in t:
            count[char] -= 1
        for val in count.values():
            if val != 0:
                return False
        return True
        

    
# @lc code=end

