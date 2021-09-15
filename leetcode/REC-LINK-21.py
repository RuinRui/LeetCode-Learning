#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   REC-LINK-21.py
@Time    :   2021/09/14 10:02:12
@Author  :   Abel
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    head = ListNode()
    cur = head
    # 解法1：递归

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:  # 递归
        if not l1:
            return l2
        if not l1:
            return l1

        res = l1 if l1.val <= l2.val else l2
        res.next = self.mergeTwoLists(res.next, l1 if l1.val <= l2.val else l2)

        return res

    # 解法2：链表
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:  # 链表
        dummy_head = ListNode()
        cur = dummy_head

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        if l1:
            cur.next = l1
        else:
            cur.next = l2

        return dummy_head.next


if __name__ == '__main__':
    s = Solution()
