#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
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
# @lc code=end
