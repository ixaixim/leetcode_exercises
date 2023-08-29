# @before-stub-for-debug-begin
from python3problem49 import *
from typing import *
# @before-stub-for-debug-end
from collections import defaultdict

#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_to_list = defaultdict(list) 
        
        for word in strs:
            key = ''.join(sorted(word)) 
            word_to_list[key].append(word)
        return list(word_to_list.values())

# PYTHON TO KNOW:
# - defaultdict(list) creates an empty dictionary, where if we try to access non-existent keys, the key is created and returns an empty list
# - sorted() returns a sorted list of characters in a string
# - join() takes a list of strings (in this case, a list of characters) and returns a single string that is the concatenation of all the strings in the iterable, separated by the string on which the method is called# @lc code=end

