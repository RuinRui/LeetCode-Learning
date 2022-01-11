from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        while right < len(nums) and left < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1

            if left < len(nums) and nums[left] != 0:
                left += 1
                right = left

            if right < len(nums) and nums[right] == 0:
                right += 1
        print(nums)


if __name__ == '__main__':
    s = Solution()
    s.moveZeroes([1, 0])
