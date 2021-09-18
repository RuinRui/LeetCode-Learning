#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   239.py
@Time    :   2021/09/18 18:12:34
@Author  :   Abel
'''
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, l = [], len(nums)
        for left in range(0, l - k + 1):
            right = left + k
            max = nums[left]
            for i in range(left, right):
                if nums[i] > max:
                    max = nums[i]

            res.append(max)

        return res


if __name__ == '__main__':
    s = Solution()
    mat = [([1, 3, -1, -3, 5, 3, 6, 7], 3)]
    for m in mat:
        print(s.maxSlidingWindow(m[0], m[1]))
