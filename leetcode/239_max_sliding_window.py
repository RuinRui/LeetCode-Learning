#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   239_.py
@Time    :   2021/09/22 16:48:05
@Author  :   Abel
'''
from typing import List
import os
import time


class MyQueue:
    def __init__(self) -> None:
        self.que = []

    def pop(self, value):
        if self.que[0] == value:
            self.que.pop(0)

    def push(self, value):
        while self.que and value > self.que[-1]:
            self.que.pop()

        self.que.append(value)

    def front(self):
        return self.que[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, l, left, max = [], len(nums), 1, nums[0]
        que = MyQueue()
        for i in range(k):
            que.push(nums[i])
        res.append(que.front())

        while left < l - k + 1:
            que.pop(nums[left - 1])
            que.push(nums[left + k - 1])
            res.append(que.front())
            left += 1

        return res

    def maxSlidingWindow_1(self, nums: List[int], k: int) -> List[int]:  # 经过剪枝的暴力超时写法
        res, l, left, max_i, max = [], len(nums), 0, -1, nums[0]
        while left < l - k + 1:
            right = left + k

            if left != 0 and nums[right - 1] >= max:
                max = nums[right - 1]
                max_i = right - 1
            else:
                if max_i >= left:
                    max = nums[max_i]
                else:
                    max = nums[left]
                    for i in range(left, right):
                        if nums[i] > max:
                            max = nums[i]
                            max_i = i
            left += 1

            res.append(max)

        return res


if __name__ == '__main__':
    s = Solution()
    mat = [([1, 3, -1, -3, 5, 3, 6, 7], 3), ([1], 1), ([1, -1], 1), ([9, 11], 2), ([4, -2], 2)]

    with open(os.path.join(os.getcwd(), 'leetcode', 'AAA_TEST_EXAMPLE', '239.txt')) as file:
        arr = file.readline().split(',')
        arr = list(map(lambda x: int(x), arr))
        k = int(file.readline())
        mat.append((arr, k))

    for m in mat:
        start = time.time()
        result = s.maxSlidingWindow(m[0], m[1])
        print(result)
        print('excute time === %f' % (time.time() - start))
