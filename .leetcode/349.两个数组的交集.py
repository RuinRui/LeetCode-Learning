#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

from typing import List
# @lc code=start


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        snap = set(nums1)
        result = set()
        for n in nums2:
            if n in snap:
                result.add(n)

        return list(result)

# @lc code=end
