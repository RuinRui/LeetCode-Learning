#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

from typing import List
# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        records = dict()
        for i, val in enumerate(nums):
            t = target - val
            if t not in records:
                records[val] = i
            else:
                return [records[t], i]
# @lc code=end
