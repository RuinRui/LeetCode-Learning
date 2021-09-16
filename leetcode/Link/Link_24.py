#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   LINK-24.py
@Time    :   2021/09/16 10:24:32
@Author  :   Abel

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

输入：head = [1,2,3,4]
输出：[2,1,4,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from Link707 import *


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(next=head)
        cur = dummy_head
        next_cur = cur.next
        while next_cur and next_cur.next:
            next_next = next_cur.next
            next_cur.next, cur.next, next_next.next = next_next.next, next_next, next_cur,

            cur = next_next.next
            if cur:
                next_cur = cur.next

        return dummy_head.next


if __name__ == '__main__':
    mylink = MyLinkedList()
    for i in range(1, 4):
        mylink.addAtTail(i)

    s = Solution()
    head = s.swapPairs(mylink.dummy_head.next)
    while head:
        print('val === ', head.val)
        head = head.next
