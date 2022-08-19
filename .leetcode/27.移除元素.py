#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

from typing import List
# @lc code=start


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        sIndex, rIndex = length - 1, 0
        # 因为sIndex始终保持着自己 != val, 所以rIndex可以=sIndex，sIndex之后的元素全都是等于val的
        while rIndex < length and rIndex <= sIndex:
            if nums[rIndex] != val:
                rIndex += 1
            else:
                if nums[sIndex] == val:
                    sIndex -= 1
                else:
                    nums[sIndex], nums[rIndex] = nums[rIndex], nums[sIndex]
                    sIndex -= 1

        return rIndex


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    result = s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    print(result)
