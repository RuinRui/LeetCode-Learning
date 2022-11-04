#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
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


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que = deque()
        que.append(p)
        que.append(q)

        while que:
            # 只要连续的两个数值一样就是对称的，因为我们加入队列的顺序是按对称加入的
            pNode, qNode = que.popleft(), que.popleft()
            if not pNode and not qNode:  # 两个都为空也是对称的
                continue
            if not pNode or not qNode:  # 只有一个为空，则不行
                return False
            if qNode.val != pNode.val:
                return False
            # 对称加入各个节点
            que.append(pNode.left)
            que.append(qNode.left)
            que.append(qNode.right)
            que.append(pNode.right)

        return True
# @lc code=end
