#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

from asyncio.windows_events import NULL


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(next=head)  # 添加一个虚拟节点
        cur = dummy_head

        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next  # 删除cur.next节点
            else:
                cur = cur.next

        return dummy_head.next

# @lc code=end
