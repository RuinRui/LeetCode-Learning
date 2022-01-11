

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        nums1, nums2 = [], []
        while left <= right:
            if nums[left] <= 0:
                nums1.append(nums[left] ** 2)
                left += 1
            if nums[right] > 0:
                nums2.append(nums[right] ** 2)
                right -= 1

        if len(nums2) == 0:
            nums1.reverse()
            return nums1
        if len(nums1) == 0:
            nums2.reverse()
            return nums2
        else:
            nums3 = []
            left1, left2 = len(nums1) - 1, len(nums2) - 1
            while left1 >= 0 and left2 >= 0:
                if nums1[left1] <= nums2[left2]:
                    nums3.append(nums1[left1])
                    left1 -= 1
                else:
                    nums3.append(nums2[left2])
                    left2 -= 1

            if left1 >= 0:
                nums3.extend(nums1[:(left1+1)])
            if left2 >= 0:
                nums3.extend(nums2[:(left2+1)])
            return nums3


if __name__ == '__main__':
    s = Solution()
    print(s.sortedSquares([0]))
