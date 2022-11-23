#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        que, result = [], []
        cur, pre, minValue = root, None, 0

        while cur or que:
            if cur:
                que.append(cur)
                cur = cur.left
            else:
                node = que.pop()
                result.append(node.val)
                if pre:
                    minValue = min(abs(node.val - pre.val), minValue)

                pre = node
                cur = node.right

        return minValue


class Solution1:  # 和
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        que, result = [], []
        cur, pre, minValue = root, None, 0

        while cur or que:
            if cur:
                que.append(cur)
                cur = cur.left
            else:
                node = que.pop()
                result.append(node.val)
                if pre:
                    minValue = min(abs(node.val - pre.val), minValue)

                pre = node
                cur = node.right

        return minValue


# @lc code=end
