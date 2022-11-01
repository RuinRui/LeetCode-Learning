#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
#

# @lc code=start

# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue, depth = deque(), 0
        if root:
            queue.append(root)
        while queue:
            size = len(queue)
            depth += 1
            for i in range(size):
                node = queue.popleft()
                for j in range(len(node.children)):
                    if node.children[j]:
                        queue.append(node.children[j])
        return depth
# @lc code=end
