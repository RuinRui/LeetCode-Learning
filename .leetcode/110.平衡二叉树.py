#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def calDepth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            lDepth = calDepth(node.left)
            # -1 表示非平衡二叉树
            if lDepth == -1:
                return -1
            lDepth += 1
            # 返回时在+1，计算节点的高度
            rDepth = calDepth(node.right)
            if rDepth == -1:
                return -1
            rDepth += 1

            return -1 if abs(rDepth - lDepth) > 1 else max(rDepth, lDepth)

        return False if calDepth(root) == -1 else True
# @lc code=end
