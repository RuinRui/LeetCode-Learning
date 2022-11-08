#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # 送分题
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def leftLeavesSum(node: Optional[TreeNode], sum: int, left: bool) -> int:
            if left and not node.left and not node.right:
                return sum + node.val

            if node.left:
                sum = leftLeavesSum(node.left, sum, True)
            if node.right:
                sum = leftLeavesSum(node.right, sum, False)

            return sum

        return leftLeavesSum(root, 0, False)


# @lc code=end
