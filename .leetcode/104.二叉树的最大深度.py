#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def digDeep(node: Optional[TreeNode], deep: int, maxDepth: int) -> int:
            if not node:
                if deep > maxDepth:
                    maxDepth = deep
                return maxDepth
            deep += 1
            # 保留上一个节点的深度，留给右侧的遍历用
            tmpDeep = deep
            maxDepth = digDeep(node.left, deep, maxDepth)
            maxDepth = digDeep(node.right, tmpDeep, maxDepth)
            return maxDepth

        return digDeep(root, 0, 0)
# @lc code=end
