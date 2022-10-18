#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return None

        if self.stack_out:
            return self.stack_out.pop()
        else:
            for _ in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())

            return self.stack_out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        res = self.pop()
        self.stack_out.append(res)

        return res

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (self.stack_out or self.stack_in)


# @lc code=end
if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(3)
    obj.push(4)
    obj.push(5)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()

    print(param_2, param_3, param_4)
