#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def sumOfLeavePath(node: Optional[TreeNode], targetSum: int, sum: int):
            sum += node.val

            if node.left:
                result = sumOfLeavePath(node.left, targetSum, sum)
                if result:
                    return result

            if node.right:
                result = sumOfLeavePath(node.right, targetSum, sum)
                if result:
                    return result

            if not node.left and not node.right:  # 叶子节点
                return True if sum == targetSum else False

            return False

        return sumOfLeavePath(root, targetSum, 0)
# @lc code=end
