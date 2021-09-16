#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   Link142.py
@Time    :   2021/09/16 14:31:34
@Author  :   Abel

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

进阶：

你是否可以使用 O(1) 空间解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from Link707 import *


class Solution:

    # 补充下思路，其实这道题对数学要求比较高，链表还是那个链表，先看下循环列表
    # <-------x-------> A
    # a1 -> a2 -> a3 -> a4 -> a5 -> a6
    #                   |__z___B__y__|
    # 假设环的起始点为A，相遇点为B，A -> B长度为y, B -> A长度为z, 节点a1 -> A长度为x, 当slow与fast相遇时，走过的路程 slow = x + y
    # fast呢？fast = x + n(y + z) + y。因为fast比slow快，所以fast在遇到slow之前肯定在环里至少转了1(n >= 1)圈.
    # 而fast行走的路程是slow的两，也就是 2(x + y) = x + n(y + z) + y
    # 简化下等式也就是 x + y = n(y + z), x = (n - 1)(y+z) + z，z就是B -> A的距离
    # 如果此时设置一个节点meet = B，start = head，让两者同时移动1，直到k（k = (n - 1)(y+z) + z）步，那meet就会回到环节点，同时start也到了环节点，两者就在环节点相遇了。

    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while slow and fast.next:  # 最少有'两个'节点都有值才能构成环
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # 相遇节点，有环
                start = head
                while start != slow:
                    start = start.next  # 从头开始走(n - 1)(y+z) + z步
                    slow = slow.next  # 从相遇节点开始走(n - 1)(y+z) + z步

                return slow

        return None
