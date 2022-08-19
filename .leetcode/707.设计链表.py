#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head, self.tail = Node(0), Node(0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.count = 0

    def _update(self, prev: Node, next: Node, val: int):
        node = Node(val)
        prev.next, next.prev = node, node
        node.next, node.prev = next, prev
        self.count += 1

    def _getNode(self, index: int) -> Node:
        snode, i = self.head.next, 0  # 寻找的节点
        while snode:
            if i == index:
                return snode
            i += 1
            snode = snode.next

        return Node(-1)

    def _checkExist(self, index: int) -> bool:
        if index >= 0 and index < self.count:
            return True
        return False

    def get(self, index: int) -> int:
        if self._checkExist(index):
            return self._getNode(index).val
        return -1

    def addAtHead(self, val: int) -> None:
        self._update(self.head, self.head.next, val)

    def addAtTail(self, val: int) -> None:
        self._update(self.tail.prev, self.tail, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return
        elif index <= 0:
            self._update(self.head, self.head.next, val)
        elif index == self.count:
            self._update(self.tail.prev, self.tail, val)
        else:
            if self._checkExist(index):
                nextNode = self._getNode(index)
                prevNode = nextNode.prev
                self._update(prevNode, nextNode, val)

    def deleteAtIndex(self, index: int) -> None:
        if self._checkExist(index):
            node = self._getNode(index)
            node.prev.next, node.next.prev = node.next, node.prev
            self.count -= 1
        return

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end


if __name__ == '__main__':
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    linkedList.addAtTail(3)
    linkedList.addAtIndex(1, 2)
    print(linkedList.get(1))
    linkedList.deleteAtIndex(1)
    print(linkedList.get(1))

    node = linkedList.head.next
    while node.next:
        print(node.val)
        node = node.next
