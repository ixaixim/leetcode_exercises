# @before-stub-for-debug-begin
from python3problem739 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from collections import deque
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # solution O(N) time: uses a stack
        # To find the next higher temperature for each day in an array, we traverse the array and add each value and its index to a stack. If we encounter a larger value, we keep going through the stack to remove smaller values until we find a value that is greater than the current value. This allows us to find the next higher temperature for each day in linear time complexity.

        stack = deque()
        answer = [0] * len(temperatures)

        # iterate through the array starting from the second element
        for i in range(1, len(temperatures)):
            # get the current temperature
            val = temperatures[i]
            # iterate through the stack until we find a temperature greater than the current temperature
            while stack and val > stack[-1][0]:
                # remove the last element from the stack
                last = stack.pop()
                # update the answer array with the number of days passed
                index = last[1]
                answer[index] = i - index # the days passed are the difference between current element and index
            # add the current temperature and its index to the stack
            stack.append([val, i])

        # the last elements are zero thanks to initialization
        return answer

# @lc code=end

