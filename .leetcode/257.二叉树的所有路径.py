#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
from ast import And
from typing import Any, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def getTreePath(node: Optional[TreeNode], result, path):
            path.append(str(node.val))
            # 记录进入左节点时的路径的长度，这样回溯时在进入右边就可以得到进入之前的在中间节点是的path路径, 右边再回来就不用回溯了，因为记录了中间节点的路径
            length = len(path)
            # 只有找到叶子节点时，这条路径才结束
            if not node.right and not node.left:
                result.append("->".join(path))
                return

            if node.left:  # 为了判断not right and not left，所以这里要判断为非空才进入
                getTreePath(node.left, result, path)
                path = path[:length]

            if node.right:
                getTreePath(node.right, result, path)

        result, path = [], []
        getTreePath(root, result, path)

        return result
# @lc code=end
