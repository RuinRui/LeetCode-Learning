#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

from typing import List, Optional
# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # 迭代法 左右中， 先序遍历 = 中左右 ---改变压栈顺序---> 中右左 ---翻转---> 左右中 = 后续遍历
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, st = [], []
        if not root:
            return result
        st.append(root)
        while st:
            node = st.pop()
            result.append(node.val)
            if node.left:  # 先压栈左边，因为左边的要最后出来
                st.append(node.left)
            if node.right:  # 在压栈右边
                st.append(node.right)

        result.reverse()
        return result


class Solution2:  # 递归法
    def traversal(self, node: Optional[TreeNode], result: list):
        if not node:
            return None
        self.traversal(node.left, result)
        self.traversal(node.right, result)
        result.append(node.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traversal(root, result)
        return result
# @lc code=end
