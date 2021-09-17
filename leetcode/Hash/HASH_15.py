#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   HASH_15.py
@Time    :   2021/09/17 16:53:53
@Author  :   Abel

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


from typing import List


class Solution:  # 同18题
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)  # 先排列
        length = len(snums)
        result = []

        for i, num in enumerate(snums):
            if snums[i] > 0:  # 如果最小值都大于和，则不用求解了
                break

            if i > 0 and snums[i - 1] == snums[i]:  # 当第二次for循环时，第一次snums[left] + snums[right] + snums[i]已经包含了所有和为0的情况，这时候snums[i]必须要变化，否则会导致重复
                continue

            left, right = i + 1, length - 1
            while left < right:
                sum = num + snums[left] + snums[right]  # 从左右最大最小开始加，遇到大的，右指针-1，否则左指针+1，直到遇到相等的

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                elif sum == 0:
                    result.append([snums[i], snums[left], snums[right]])
                    # 当取到想要的值时，为了防止重复数组，必须取到不同的right，因为right相同那left必相同(因为此时snums[i]固定)，而right变小后，left必须增大，才能保证和为0
                    while right > left and snums[right - 1] == snums[right]:
                        right -= 1

                    while left < right and snums[left + 1] == snums[left]:
                        left += 1

                    right -= 1
                    left += 1

        return result


if __name__ == '__main__':
    s = Solution()
    mat = [[-1, 0, 1, 2, -1, -4]]
    for m in mat:
        print(s.threeSum(m))
