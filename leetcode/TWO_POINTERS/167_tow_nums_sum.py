#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   167_tow_nums_sum.py
@Time    :   2021/12/30 12:17:06
@Author  :   Abel
'''
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        last, left, right = -1, 0, len(numbers) - 1
        mid = (left + right) // 2
        if numbers[-1] <= target:
            mid = right
        else:
            while numbers[mid] != target:
                if mid - last == 1 and numbers[mid] > target:
                    last = mid
                    mid = max(mid, last)
                    break
                elif numbers[mid] < target:
                    last = mid
                    mid = (mid + right) // 2
                elif numbers[mid] > target:
                    last = mid
                    mid = (mid + left) // 2

        for i in range(mid):
            left = i
            if numbers[left] + numbers[right] == target:
                return [left, right]
            else:
                while left < right:
                    if numbers[left] + numbers[right] > target:
                        right -= 1
                    elif numbers[left] + numbers[right] < target:
                        left += 1
                    else:
                        return [left, right]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 26))
