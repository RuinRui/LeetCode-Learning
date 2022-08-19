#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

from tkinter import N
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        virHead = ListNode(next=head)
        fast, slow, index = head, head, 0
        pre = virHead

        while fast:
            fast = fast.next
            index += 1
            if index == n:
                break

        while fast:
            fast = fast.next
            pre = slow
            slow = slow.next

        if index == n:
            pre.next = slow.next

        return virHead.next
# @lc code=end
