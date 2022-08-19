#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        front, behind = head, head.next
        head = ListNode(next=(front if behind == None else behind))
        cur = head
        while front and behind:
            front.next, behind.next = behind.next, front
            front, behind = behind, front  # 交换前后两个节点
            cur.next = front
            # 让cur先定位到交换后的最后一个节点，以便指向下一个交换的节点的前节点
            cur = front.next
            front = behind.next
            if front:
                behind = front.next
            else:
                break

        return head.next

# @lc code=end
