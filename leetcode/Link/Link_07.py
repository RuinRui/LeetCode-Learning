#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   Link07.py
@Time    :   2021/09/16 11:28:00
@Author  :   Abel

给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。

A: a1 -> a2 -> a2 \
                  c1 -> c2 -> c3   
B:       b1 -> b2 /


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from Link_707 import *


class Solution:  # 注意这里的ListNode和 leetcode不一样
    # 非常巧妙的一个解法，评论区看来的, 而且这种解法完全能避免有环(循环链表)的问题, 只需要在遍历时候判断是不是回到头节点就行，如果有其他环请参考Link142.py
    # 设交集链表长c,链表1除交集的长度为a，链表2除交集的长度为b，有a + c + b = b + c + a, 若无交集，则a + b = b + a
    # 这里解释一下，从a开始遍历，遍历会跑到b遍历, 这时候就是答主说的a + b，b在遍历完又回到a，一直遍历到相交点就是a + b + c的过程，从b开始也是如此，就是b + a + c，如果有相交点这样循环下去，肯定会有个相交的点，如果没有的话，就是a + b, b + a的最后一个点的next（null相等），太巧妙了
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA

        return ha

    # 暴力解法
    def getIntersectionNode_1(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        link_searched = set()
        while headA:
            link_searched.add(headA)
            headA = headA.next

        while headB:
            if headB in link_searched:
                return headB
            headB = headB.next

        return None
