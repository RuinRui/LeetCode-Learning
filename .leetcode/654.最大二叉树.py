#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        # 找出最大值
        max, index = -1, 0
        for i, v in enumerate(nums):
            if v > max:
                max, index = v, i

        # 分成左右两个数组
        node = TreeNode(max)
        leftNums = nums[:index]
        rightNums = nums[index + 1:]

        node.left = self.constructMaximumBinaryTree(leftNums)
        node.right = self.constructMaximumBinaryTree(rightNums)

        return node

        # @lc code=end


if __name__ == '__main__':
    s = Solution()
    result = s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    print('result >>> ', result)
