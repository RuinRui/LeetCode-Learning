class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        h1, h2 = headA, headB
        # 设两个链表h1、h2长度为A、B, 相交部分为L, 不相交的部分为A1、B1, 则必有等式A + B(B1+L) = B + A(A1+L), 也就是说从A B分别开始遍历, 如果相交则最后必定遍历到L的最后一个节点
        while h1 != h2:
            h1 = h1.next if h1 else headB
            h2 = h2.next if h2 else headA

        return h1
