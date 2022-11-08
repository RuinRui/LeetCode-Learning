#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result, maxDepth = 0, 0

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.result = root.val

        def leftLeavesNum(node: Optional[TreeNode], depth: int):
            if not node.left and not node.right:  # 叶子节点
                if self.maxDepth < depth:  # 注意这里一定要是<,因为我们按照的是中左右的顺序，左在右前面遍历到，如果左右节点是一个深度，<=的话会取到右边节点的值
                    self.maxDepth, self.result = depth, node.val
                return

            if node.left:
                leftLeavesNum(node.left, depth + 1)
            if node.right:
                leftLeavesNum(node.right, depth + 1)
            return

        leftLeavesNum(root, 0)

        return self.result

# @lc code=end
