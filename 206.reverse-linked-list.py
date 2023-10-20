# @before-stub-for-debug-begin
from python3problem206 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time complexity: O(N), N is length of linked list
        # Space complexity: O(N) since for each node creates a new Node.
        if not head:
            # case head is None
            return None
        elif not head.next:
            # case only one Node
            return head 
        # all other cases
        prevNode = ListNode(val=head.val)
        while head.next:
           # moving along the linked list
           newNode = ListNode(head.next.val, next=prevNode)
           head = head.next
           prevNode = newNode
        return newNode
    

            
    
# @lc code=end

