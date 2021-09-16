#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   Link19.py
@Time    :   2021/09/16 11:06:58
@Author  :   Abel

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from Link707 import *


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(next=head)

        slow, fast = dummy_head, dummy_head
        while(n != 0):  # fast先往前走n步
            fast = fast.next
            n -= 1

        while(fast.next != None):
            slow = slow.next
            fast = fast.next
        # fast 走到结尾后，slow的下一个节点为倒数第N个节点
        slow.next = slow.next.next  # 删除
        return dummy_head.next
