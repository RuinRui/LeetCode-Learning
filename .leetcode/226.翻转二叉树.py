#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

from collections import deque
from typing import Optional
# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # 迭代法 深度优先遍历 前序遍历 中左右 中右左都行
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        st = deque()
        st.append(root)
        while st:
            node = st.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)

        return root


class Solution3:  # 迭代法 广度优先遍历 层序遍历
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        node, st = root, []
        st.append(node)
        while st:
            for i in range(len(st)):
                n = st.pop()
                if n.left:
                    st.append(n.left)
                if n.right:
                    st.append(n.right)
                n.left, n.right = n.right, n.left

        return root


class Solution2:  # 递归法
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        def invert(node: Optional[TreeNode]):
            if not node:
                return None
            node.left, node.right = node.right, node.left
            invert(node.left)
            invert(node.right)

        node = root
        invert(node)
        return root
# @lc code=end
