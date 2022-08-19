#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

from typing import Optional
# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        while head:
            next = head.next
            head.next, pre = pre, head
            head = next

        return pre

# @lc code=end
