#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   225_my_stack.py
@Time    :   2021/09/18 14:53:22
@Author  :   Abel

请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。

实现 MyStack 类：

void push(int x) 将元素 x 压入栈顶。
int pop() 移除并返回栈顶元素。
int top() 返回栈顶元素。
boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。
 

注意：

你只能使用队列的基本操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-stack-using-queues
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import collections


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.que.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        size = len(self.que)
        if not size:
            return None

        while size != 1:
            self.que.append(self.que.pop())
            size -= 1

        return self.que.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        res = self.pop()
        self.que.append(res)

        return res

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.que


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

if __name__ == '__main__':
    s = MyStack()
