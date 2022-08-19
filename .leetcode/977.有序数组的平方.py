#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

from typing import List
# @lc code=start


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        k = right
        result = [0 for i in nums]
        while left <= right:  # 这里要<=，因为left=right时候也是一个值，这个值也要加到数组里，这时候k应该=0
            l, r = nums[left] * nums[left], nums[right] * nums[right]
            if l <= r:
                right -= 1
                result[k] = r
            else:
                left += 1
                result[k] = l
            k -= 1

        return result
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    result = s.sortedSquares([-4, -1, 0, 3, 10])
    print(result)
    result = s.sortedSquares([-7, -3, 2, 3, 11])
    print(result)
