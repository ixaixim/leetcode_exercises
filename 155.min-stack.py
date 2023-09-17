# @before-stub-for-debug-begin
from python3problem155 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
from collections import deque
# @lc code=start
class MinStack:
    # idea: use a stack of dicts: every element of the dict contains the value and the current minimum in the stack.
    # Time complexity for every function: O(1)
    # Space complexity: O(2N) (have to store both the value and the min so far for each element)
    # for some reason my code does not work .-. and cannot debug this.
    # def __init__(self):
    #     self.stack = deque()

    # def push(self, val: int) -> None:
    #     if not self.stack:
    #         self.stack.append((val, val))
    #     minimum = min(self.stack[-1][1], val)
    #     self.stack.append((val, minimum))

    # def pop(self) -> None:
    #     if self.stack:
    #         self.stack.pop()

    # def top(self) -> int:
    #     if not self.stack:
    #         return 0
    #     return self.stack[-1][0]

    # def getMin(self) -> int:
    #     if not self.stack:
    #         return 0
    #     return self.stack[-1][1]
    def __init__(self):
        self.stack = []

    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
        else:
            mn = min(self.stack[-1][1], val)
            self.stack.append((val, mn))

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        return 0

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return 0


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

