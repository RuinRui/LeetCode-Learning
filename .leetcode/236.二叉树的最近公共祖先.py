#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 解法1: 以中序遍历，存储所有中间节点，直到找到第一个节点为止，然后以所有中间节点为根遍历，寻找另一个节点，找到则是此中间节点，n^2，有点粗暴，略
    # 解法2:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif left and not right:
            return left
        elif right and not left:
            return right

        return None

# @lc code=end
