#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # 题目和104差不多，只需要判断 左右子节点都为空的时候 这个节点就到底就行了
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def calDepth(node: TreeNode, deep: int, minDepth: int) -> int:
            if not node.left and not node.right:
                minDepth = deep if deep < minDepth else minDepth

            if node.left:
                minDepth = calDepth(node.left, deep + 1, minDepth)
            if node.right:
                minDepth = calDepth(node.right, deep + 1, minDepth)

            return minDepth

        return calDepth(root, 1, 10**5)

# @lc code=end
