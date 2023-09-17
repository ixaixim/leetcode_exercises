# @before-stub-for-debug-begin
from python3problem22 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # had no idea how it worked, solution by: https://leetcode.com/problems/generate-parentheses/solutions/2712761/beautiful-iterative-python-solution-with-stack/
        # There are many ways to solve this problem, but this one chooses the stack.


        # 1. The items in the stack are tuples with the following makeup: [parenthesis string, open remaining, closed remaining].
        # We initialize the stack with ["(",n-1,n] because every valid parenthesis combination starts with "(".
        rv = []
        stack = [("(", n-1,n)]
        # 2. Once an item x is popped from the stack, we check if it is complete by checking if the number of open remaining (i.e. 'o') and closed remaining (i.e. 'c') are zero. If it is complete, we append the string stored in x[0] to the return array.
        while stack:
            item = stack.pop()

            s= item[0]
            o = item[1] 
            c = item[2]

            if o == 0 and c ==0: 
                rv.append(s) # this is triggered every time a valid combination of parenthesis is in the stack.
            else: 
                # add "(" as long as we need opens and add ")" as long as a "(" is created. 
                if o != 0:
                    stack.append([s+"(", o-1, c]) 
                if o < c: 
                    stack.append([s+")", o, c-1])

        return rv

# @lc code=end

