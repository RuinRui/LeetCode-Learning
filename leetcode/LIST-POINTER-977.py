#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   LIST-POINTER-977.py
@Time    :   2021/09/16 09:44:52
@Author  :   Abel
'''

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right, index = 0, n - 1, n - 1
        ans = [-1] * n
        while left <= right:
            lm = nums[left] ** 2
            rm = nums[left] ** 2
            if lm > rm:
                ans[index] = lm
                left += 1
            else:
                ans[index] = rm
                left -= 1
            index -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    result = s.sortedSquares([-5, -3, -2, -1])
    print(result)
