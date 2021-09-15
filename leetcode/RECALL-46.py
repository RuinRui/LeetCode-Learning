#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   RECALL-46.py
@Time    :   2021/09/14 18:09:35
@Author  :   Abel
'''

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.backtracking(nums, [False]*len(nums), len(nums), [], [])

    def backtracking(self, nums: List[int], used: List[bool], k: int, path: list, result: list):
        if k == len(path):
            result.append(path[:])
            return

        for i, num in enumerate(nums):
            if used[i]:
                continue
            path.append(num)
            used[i] = True
            self.backtracking(nums, used, k, path, result)
            path.pop(-1)
            used[i] = False

        return result


if __name__ == '__main__':
    s = Solution()
    for nums in [[1, 2, 3]]:
        result = s.permute(nums)
        print(result)
