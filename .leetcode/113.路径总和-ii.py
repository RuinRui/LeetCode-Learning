#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result, path = [], []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        # leetcode会多次调用这个方法，所以把类变量清空一下
        self.result.clear()
        self.path.clear()

        def sumOfLeavePath(node: Optional[TreeNode], targetSum: int, sum: int):
            sum += node.val
            self.path.append(node.val)
            if node.left:
                sumOfLeavePath(node.left, targetSum, sum)
                self.path.pop()

            if node.right:
                sumOfLeavePath(node.right, targetSum, sum)
                self.path.pop()

            if not node.left and not node.right:  # 叶子节点
                if sum == targetSum:
                    self.result.append(self.path[:])

            return

        sumOfLeavePath(root, targetSum, 0)

        return self.result

# @lc code=end
