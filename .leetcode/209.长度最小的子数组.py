#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

from typing import List
# @lc code=start


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, minSize, sum, subLength = 0, 100001, 0, 0

        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                subLength = i - start + 1
                minSize = minSize if minSize < subLength else subLength
                sum -= nums[start]
                start += 1

        return minSize if minSize != 100001 else 0


# @lc code=end

if __name__ == '__main__':
    s = Solution()
    result = s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print(result)
    result = s.minSubArrayLen(4, [1, 4, 4])
    print(result)
    result = s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1])
    print(result)
