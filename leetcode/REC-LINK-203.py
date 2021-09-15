#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   REC-LINK-203.py
@Time    :   2021/09/15 15:42:16
@Author  :   Abel
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(next=head)
        cur = dummy_head

        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy_head.next
