#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start
# Definition for singly-linked list.


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                behind = head
                while slow != behind:
                    slow = slow.next
                    behind = behind.next

                return behind

        return None


# @lc code=end
