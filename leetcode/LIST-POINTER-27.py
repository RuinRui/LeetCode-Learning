#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   LIST-27.py
@Time    :   2021/09/15 11:25:15
@Author  :   Abel
'''

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i - index] == val:
                nums.pop(i - index)
                index += 1

        return len(nums)
