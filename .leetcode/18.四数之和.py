#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

from typing import List
# @lc code=start


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        count = len(nums)
        nums.sort()
        result = []

        for i, a in enumerate(nums[:-3]):
            if a > target and (target >= 0 or a >= 0):
                break
            if i >= 1 and nums[i - 1] == nums[i]:  # 对a去重
                continue
            for j in range(i+1, count - 2):
                b = nums[j]
                if a + b > target and (target >= 0 or (a + b) >= 0):
                    break
                if j > i + 1 and nums[j - 1] == nums[j]:  # 对b去重
                    continue
                left, right = j + 1, count - 1
                while right > left:
                    c, d = nums[left], nums[right]
                    if a + b + c + d == target:
                        result.append([a, b, c, d])
                        #对c, d去重
                        while right > left and nums[left + 1] == nums[left]:
                            left += 1
                        while right > left and nums[right - 1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif a + b + c + d > target:
                        right -= 1
                    elif a + b + c + d < target:
                        left += 1
        return result


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    result = s.fourSum([1, 0, -1, 0, -2, 2], 0)
    print(result)
