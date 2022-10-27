#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

from turtle import left
from typing import List, Optional
# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # 迭代法 中左右
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes, result = [], []
        if not root:
            return result

        nodes.append(root)
        while nodes:
            node = nodes.pop()
            result.append(node.val)
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)

        return result


class Solution2:  # 递归法
    def traversal(self, node: Optional[TreeNode], result: list):
        if not node:
            return None
        result.append(node.val)
        self.traversal(node.left, result)
        self.traversal(node.right, result)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traversal(root, result)
        return result

# @lc code=end
