#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   LINK-707.py
@Time    :   2021/09/15 15:53:56
@Author  :   Abel

设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class LinkNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy_head = LinkNode()
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        dummy_head = self.dummy_head
        head, i = dummy_head, -1
        while i < index and head.next:
            head = head.next
            i += 1

        return head.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = LinkNode(val)
        if self.dummy_head.next:
            new_head.next = self.dummy_head.next

        self.dummy_head.next = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        head = self.dummy_head
        while head.next:
            head = head.next

        tail = LinkNode(val)
        head.next = tail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return

        dummy_head = self.dummy_head
        head, i = dummy_head, 0
        while head.next and i < index:
            head = head.next
            i += 1

        insert = LinkNode(val)
        if i > index:
            return

        insert = LinkNode(val)
        insert.next = head.next
        head.next = insert

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size:
            return

        dummy_head = self.dummy_head
        head, i = dummy_head, 0
        while i < index and head.next:
            i += 1
            head = head.next

        if i == index and head:
            head.next = head.next.next
            self.size -= 1


if __name__ == '__main__':
    # Your MyLinkedList object will be instantiated and called as such:
    linkedList = MyLinkedList()
    linkedList.addAtTail(1)  # 1
    linkedList.get(0)
    linkedList.addAtHead(7)  # 7 1
    linkedList.addAtHead(2)  # 2 7 1
    linkedList.addAtHead(1)  # 1 2 7 1
    linkedList.addAtIndex(3, 0)  # 1 2 7 0 1
    linkedList.deleteAtIndex(2)  # 1 2 0 1
    linkedList.addAtHead(6)  # 6 1 2 0 1
    linkedList.addAtTail(4)  # 6 1 2 0 1 4
    linkedList.get(4)  # 4
    linkedList.addAtHead(4)  # 4 6 1 2 0 1 4
    linkedList.addAtIndex(5, 0)  # 4 6 1 2 0 0 1 4
    linkedList.addAtHead(6)  # 6 4 6 1 2 0 0 1 4
    linkedList.get(0)  # 6 4 6 1 2 0 0 1 4
    linkedList.deleteAtIndex(8)  # 6 4 6 1 2 0 0 1 4

    head = linkedList.dummy_head
    index = 0
    while head.next:
        head = head.next
        print(head.val)
        # print(linkedList.get(index))
        index += 1
