#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
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
    def __init__(self) -> None:
        self.parent = None

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            if root.right and not root.left:
                return root.right
            elif root.left and not root.right:
                return root.left
            elif not root.right and not root.left:
                return None
            elif root.right and root.left:
                node = root.right
                while node:
                    if node.left is None:
                        break
                    node = node.left
                node.left = root.left
                return root.right

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root
# @lc code=end
