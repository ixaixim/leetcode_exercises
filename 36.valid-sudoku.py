# @before-stub-for-debug-begin
from python3problem36 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
from collections import defaultdict
# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # This code solves the Sudoku problem in O(N^2) time complexity by iterating through each row and column of the board. It uses a dictionary of sets, one for each column/row/box, to check for duplicates in constant time. The worst space complexity of this approach is O(N^2), since we add to the set inside the nested loop.        
        box_number = lambda r,c: 3*(r//3) + (c//3) # r row number, c col number
        hash_map_box = defaultdict(set)
        hash_map_col = defaultdict(set)
        hash_map_row = defaultdict(set)

        for r in range(9):
            for c, val in enumerate(board[r]):
                if val == '.':
                    continue
                val = int(val)
                box_index = box_number(r,c)
                if (
                    (val in hash_map_box[box_index]) or 
                    (val in hash_map_col[c]) or 
                    (val in hash_map_row[r])):
                    return False
                hash_map_box[box_index].add(val)
                hash_map_col[c].add(val)
                hash_map_row[r].add(val)

        return True
# @lc code=end

