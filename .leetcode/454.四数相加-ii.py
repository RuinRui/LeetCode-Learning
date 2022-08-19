#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

from typing import List
# @lc code=start


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        count = 0
        sum1 = dict()
        for v1 in nums1:
            for v2 in nums2:
                sum = v1 + v2
                if sum not in sum1:
                    sum1[sum] = 1
                else:
                    sum1[sum] += 1

        for v1 in nums3:
            for v2 in nums4:
                target = -v1 - v2
                if target in sum1:
                    count += sum1[target]

        return count


# @lc code=end
