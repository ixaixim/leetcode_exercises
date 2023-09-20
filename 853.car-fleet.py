# @before-stub-for-debug-begin
from python3problem853 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#
from collections import deque
# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # the problem is very poorly phrased.
        # note: have to keep track of the time needed to arrive at location.
        # Sort the cars from closest to farthest to target.
        # Add car to stack if the time to reach target is longer than time of car ahead (i.e. at top of the stack)
        stack = deque(maxlen=len(position)) # can set a maxlen here
        for pos, vel in sorted(zip(position, speed), reverse=True):
            dist = target - pos
            print(pos)
            if not stack:   stack.append(dist / vel)
            else:
                if dist / vel > stack[-1]:
                    stack.append(dist / vel)
        return len(stack)
# @lc code=end

