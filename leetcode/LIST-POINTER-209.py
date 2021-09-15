#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   LIST-POINTER-209.PY
@Time    :   2021/09/15 11:26:48
@Author  :   Abel
'''
from typing import List
from functools import reduce


class Solution:  # 滑动窗口经典题，没啥好说的
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length, left, right, sum, index = 99999, 0, 0, 0, 0
        nlength = len(nums)
        for i in range(nlength):
            sum += nums[i]
            right = i
            while sum >= target:
                length = min(length, i - left + 1)
                sum -= nums[left]
                left += 1

        return length if length != 99999 else 0


if __name__ == '__main__':
    s = Solution()
    nums = [[2, 3, 1, 2, 4, 3],
            [1, 4, 4],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]]
    targets = [7, 4, 11, 213]
    for i, num in enumerate(nums):
        print(targets[i], num)
        print(s.minSubArrayLen(targets[i], num))
