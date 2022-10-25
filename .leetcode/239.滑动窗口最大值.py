#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
from collections import deque
from typing import List
# @lc code=start

# 单调递减队列，保证当前k个数中可能最大的数在队列中(因为移除的时候会判断是否会移除最大的)，每次push的时候都会检查是否是最大的数，如果是，则移除所有小于他的数，保证队列里始终是单调递减的


class DescQueue:
    def __init__(self) -> None:
        self.queue = deque()

    def pop(self, value: int):
        if self.queue and self.queue[0] == value:
            self.queue.popleft()

    def push(self, value: int):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()

        self.queue.append(value)

    def front(self) -> int:
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = DescQueue()
        arr = []
        for i in range(k):
            queue.push(nums[i])

        arr.append(queue.front())
        for i in range(k, len(nums)):
            num = nums[i]
            abort = i - k
            queue.pop(nums[abort])
            queue.push(num)
            arr.append(queue.front())

        return arr


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    result = s.maxSlidingWindow([1, 3, 10, -3, 5, 8, 6, 7], 3)
    print(result)
    s = Solution()
    result = s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print(result)
