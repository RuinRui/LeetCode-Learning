#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

from typing import List, Optional
# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # 迭代法 左中右
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, st = [], []
        cur = root
        while cur or st:
            if cur:
                st.append(cur)
                cur = cur.left
            else:
                node = st.pop()
                result.append(node.val)
                cur = node.right

        return result


class Solution2:  # 递归法
    def traversal(self, node: Optional[TreeNode], result: list):
        if not node:
            return None
        self.traversal(node.left, result)
        result.append(node.val)
        self.traversal(node.right, result)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traversal(root, result)
        return result

# @lc code=end
