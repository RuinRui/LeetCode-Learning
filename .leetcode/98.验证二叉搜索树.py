#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # 中序遍历正好可以解决，左中右的顺序遍历，左永远小于中，中永远小于右，二叉搜索树的中序遍历就是一个有序队列
    def __init__(self) -> None:
        self.maxValue = -2**32

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.isValidBST(root.left)
        if not left:
            return left
        # 在这里处理看看是否是从小到大排列
        if root.val > self.maxValue:
            self.maxValue = root.val
        else:
            return False

        right = self.isValidBST(root.right)
        if not right:
            return right

        return right and left


# @lc code=end
