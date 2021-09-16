#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   REC-LINK-206.py
@Time    :   2021/09/14 11:57:45
@Author  :   Abel
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 解法1 常规循环
    def reverseList(self, head: ListNode) -> ListNode:
        result, result_next = None, None
        while head:
            next = head.next
            result = head
            result.next = result_next
            head = next
            result_next = result

        return result
    # 解法2 递归

    def reverseList1(self, head: ListNode) -> ListNode:
        return self.reverse_l(head, None)

    def reverse_l(self, head: ListNode, last: ListNode) -> ListNode:
        if not head:
            return last
        next = head.next
        head.next = last
        head = self.reverse_l(next, head)
