#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # 几种遍历都可以，直接累加个数就行，这里写个按照完全二叉树的写法
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left, right = root.left, root.right
        leftDepth, rightDepth = 0, 0
        # 遍历左节点
        while left:
            leftDepth += 1
            left = left.left

        # 遍历右节点
        while right:
            rightDepth += 1
            right = right.right

        if rightDepth == leftDepth:  # 如果左右节点深度相等，那么在满二叉树的前提下，个数肯定是2**Depth - 1(特殊情况Depth = 1，个数为1), 而且满二叉树总有一个地方是满足这个条件的
            return (2 << rightDepth) - 1

        leftDepth = self.countNodes(root.left)
        rightDepth = self.countNodes(root.right)
        return leftDepth + rightDepth + 1  # 1是加的回溯的中间节点


class Solution2:  # 简单举例，层序遍历
    def countNodes(self, root: Optional[TreeNode]) -> int:
        queue, count = deque(), 0
        if root:
            queue.append(root)

        while queue:
            size = len(queue)
            count += size
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return count

# @lc code=end
