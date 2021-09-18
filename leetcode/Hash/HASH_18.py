#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   HASH_18.py
@Time    :   2021/09/17 10:03:35
@Author  :   Abel
'''

import collections
from typing import Counter, DefaultDict, List
import time


class Solution:  # 同15题
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        snums = sorted(nums)
        length = len(snums)
        result = []

        for i, n1 in enumerate(snums):
            if i > 0 and snums[i - 1] == snums[i]:
                continue

            for j in range(i + 1, length):
                if j > i + 1 and snums[j - 1] == snums[j]:
                    continue

                left, right, n2 = j + 1, length - 1, snums[j]

                while left < right:
                    sum = n1 + n2 + snums[left] + snums[right]

                    if sum > target:
                        right -= 1
                    elif sum < target:
                        left += 1
                    elif sum == target:
                        result.append([n1, n2, snums[left], snums[right]])

                        while right > left and snums[right - 1] == snums[right]:
                            right -= 1

                        while left < right and snums[left + 1] == snums[left]:
                            left += 1

                        right -= 1
                        left += 1

        return result


if __name__ == '__main__':
    s = Solution()
    mat = [([-3, -1, 0, 2, 4, 5], 1),
           ([2, -4, -5, -2, -3, -5, 0, 4, -2], -14),
           ([2, 2, 2, 2], 8),
           ([1, 0, -1, 0, -2, 2], 0),
           ([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
            2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 8),
           ([-3, 0, 7, -2, -6, -5, 1, 5, -1, -8, -9, -8, 7, 1, 1, 3, 1, 10], 0)]

    for m in mat:
        result = s.fourSum(m[0], m[1])
        print(result)
